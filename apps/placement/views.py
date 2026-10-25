from collections import defaultdict

from django.shortcuts import redirect, render

from apps.accounts.models import CEFRLevel
from apps.courses.models import Level

from .models import PlacementChoice, PlacementQuestion

LEVEL_ORDER = [code for code, _ in CEFRLevel.choices]
PASS_RATIO = 2 / 3


def recommend_level(results):
    """results: {level: (correct, total)}. Start at the first level not passed."""
    for code in LEVEL_ORDER:
        correct, total = results.get(code, (0, 0))
        if total and correct / total < PASS_RATIO:
            return code
    passed = [code for code in LEVEL_ORDER if results.get(code, (0, 0))[1]]
    return passed[-1] if passed else CEFRLevel.A1


def test(request):
    questions = PlacementQuestion.objects.prefetch_related("choices").order_by("order", "id")
    if request.method != "POST":
        return render(request, "placement/test.html", {"questions": questions})

    picked_ids = [v for k, v in request.POST.items() if k.startswith("q") and v.isdigit()]
    correct_ids = set(
        PlacementChoice.objects.filter(pk__in=picked_ids, is_correct=True).values_list("question_id", flat=True)
    )
    tally = defaultdict(lambda: [0, 0])
    for q in questions:
        tally[q.level][1] += 1
        if q.id in correct_ids:
            tally[q.level][0] += 1
    results = {code: tuple(v) for code, v in tally.items()}
    level_code = recommend_level(results)

    if request.user.is_authenticated:
        request.user.level = level_code
        request.user.save(update_fields=["level"])
    else:
        request.session["placement_level"] = level_code
    request.session["placement_result"] = {
        "level": level_code,
        "correct": sum(c for c, _ in results.values()),
        "total": sum(t for _, t in results.values()),
        "by_level": [[code, *results[code]] for code in LEVEL_ORDER if code in results],
    }
    return redirect("placement:result")


def result(request):
    data = request.session.get("placement_result")
    if not data:
        return redirect("placement:test")
    level = Level.objects.filter(code=data["level"]).first()
    return render(request, "placement/result.html", {"result": data, "level": level})
