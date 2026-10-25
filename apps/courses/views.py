import json

from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count, Prefetch, Q
from django.http import Http404, HttpResponseBadRequest, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.http import require_POST

from .models import Choice, Exercise, Lesson, LessonProgress, Level, UserMistake

PASS_SCORE = 60


def completed_lesson_ids(user):
    if not user.is_authenticated:
        return set()
    return set(
        LessonProgress.objects.filter(user=user, completed_at__isnull=False).values_list("lesson_id", flat=True)
    )


def level_list(request):
    levels = Level.objects.annotate(
        lesson_count=Count("units__lessons", distinct=True, filter=Q(units__lessons__is_published=True)),
        unit_count=Count("units", distinct=True),
    )
    done = completed_lesson_ids(request.user)
    rows = []
    for level in levels:
        level_done = Lesson.objects.filter(unit__level=level, id__in=done).count() if done else 0
        rows.append({"level": level, "done": level_done})
    return render(request, "courses/level_list.html", {"rows": rows})


def level_detail(request, code):
    level = get_object_or_404(Level, code=code.upper())
    units = level.units.prefetch_related(
        Prefetch("lessons", queryset=Lesson.objects.filter(is_published=True).annotate(exercise_count=Count("exercises")))
    )
    return render(
        request,
        "courses/level_detail.html",
        {"level": level, "units": units, "done": completed_lesson_ids(request.user)},
    )


def listening(request):
    lessons = (
        Lesson.objects.filter(is_published=True, kind=Lesson.Kind.LISTENING)
        .select_related("unit__level")
        .annotate(exercise_count=Count("exercises"))
    )
    return render(
        request, "courses/listening.html", {"lessons": lessons, "done": completed_lesson_ids(request.user)}
    )


REVIEW_QUESTIONS = 2
MISTAKES_BATCH = 10
MISTAKE_XP = 2


def serialize_exercise(exercise, review_of=None):
    data = {
        "id": exercise.id,
        "type": exercise.type,
        "instruction": exercise.instruction or exercise.get_type_display(),
        "prompt": exercise.prompt,
        "audio": exercise.audio_text,
    }
    if review_of:
        data["review"] = review_of
    if exercise.type == Exercise.Type.CHOICE:
        data["choices"] = [{"id": c.id, "text": c.text} for c in exercise.choices.all()]
    elif exercise.type == Exercise.Type.ORDER:
        data["words"] = exercise.word_tiles()
    return data


def accessible_exercises(user):
    """Exercises in published lessons the user may open."""
    qs = Exercise.objects.filter(lesson__is_published=True)
    if not (user.is_authenticated and user.is_premium):
        qs = qs.filter(lesson__is_premium=False)
    return qs


def review_exercises(user, lesson):
    """A few questions from lessons the learner already finished: spaced, interleaved retrieval."""
    if not user.is_authenticated:
        return []
    return list(
        accessible_exercises(user)
        .filter(lesson__progress__user=user, lesson__progress__completed_at__isnull=False)
        .exclude(lesson=lesson)
        .select_related("lesson")
        .prefetch_related("choices")
        .order_by("?")[:REVIEW_QUESTIONS]
    )


def lesson_detail(request, slug):
    lesson = get_object_or_404(
        Lesson.objects.select_related("unit__level").filter(is_published=True), slug=slug
    )
    if lesson.is_locked_for(request.user):
        return render(request, "courses/lesson_locked.html", {"lesson": lesson})

    exercises = list(lesson.exercises.prefetch_related("choices"))
    review = review_exercises(request.user, lesson) if exercises else []
    siblings = list(Lesson.objects.filter(unit=lesson.unit, is_published=True).values_list("slug", flat=True))
    index = siblings.index(lesson.slug)
    next_lesson = (
        Lesson.objects.filter(is_published=True, slug=siblings[index + 1]).first()
        if index + 1 < len(siblings)
        else Lesson.objects.filter(is_published=True, unit__level=lesson.unit.level, unit__order__gt=lesson.unit.order)
        .order_by("unit__order", "order")
        .first()
    )
    progress = None
    if request.user.is_authenticated:
        progress = LessonProgress.objects.filter(user=request.user, lesson=lesson).first()

    intro = f"{len(exercises)} задачи, около {lesson.minutes} минути. Нужни са ти поне {PASS_SCORE}% верни отговора."
    if review:
        intro += f" Започваме с {len(review)} въпроса за преговор от предишни уроци."
    context = {
        "lesson": lesson,
        # Review questions first (warm-up), then the lesson's own exercises.
        "exercises_json": [serialize_exercise(e, review_of=e.lesson.title) for e in review]
        + [serialize_exercise(e) for e in exercises],
        "dialogue": lesson.dialogue_lines(),
        "exercise_count": len(exercises),
        "next_lesson": next_lesson,
        "progress": progress,
        "position": index + 1,
        "unit_size": len(siblings),
        "complete_url": reverse("courses:complete", args=[lesson.slug]),
        "intro_text": intro,
        "done_url": next_lesson.get_absolute_url() if next_lesson else lesson.unit.level.get_absolute_url(),
        "done_label": "Следващ урок" if next_lesson else f"Към {lesson.unit.level.code}",
    }
    return render(request, "courses/lesson_detail.html", context)


def parse_json(request):
    try:
        return json.loads(request.body or b"{}")
    except (ValueError, UnicodeDecodeError):
        return None


def record_attempt(user, exercise, correct):
    """Keep the learner's mistakes deck up to date."""
    if not user.is_authenticated:
        return
    now = timezone.now()
    if correct:
        UserMistake.objects.filter(user=user, exercise=exercise, resolved_at__isnull=True).update(resolved_at=now)
        return
    mistake, created = UserMistake.objects.get_or_create(user=user, exercise=exercise)
    if not created:
        mistake.wrong_count += 1
        mistake.last_wrong_at = now
        mistake.resolved_at = None
        mistake.save(update_fields=["wrong_count", "last_wrong_at", "resolved_at"])


def check_response(request, exercise, answer):
    correct = exercise.is_correct_answer(answer)
    record_attempt(request.user, exercise, correct)
    response = {"correct": correct, "explanation": exercise.explanation}
    if exercise.type == Exercise.Type.CHOICE:
        response["correct_choice"] = (
            Choice.objects.filter(exercise=exercise, is_correct=True).values_list("id", flat=True).first()
        )
    response["correct_answer"] = (exercise.accepted_answers() or [""])[0]
    return JsonResponse(response)


@require_POST
def check_any(request):
    """Check one answer for any exercise the user can access (lesson, review or mistakes practice)."""
    data = parse_json(request)
    if data is None:
        return HttpResponseBadRequest("invalid json")
    exercise = get_object_or_404(accessible_exercises(request.user), pk=data.get("exercise"))
    return check_response(request, exercise, data.get("answer", ""))


@require_POST
def check_exercise(request, slug):
    data = parse_json(request)
    if data is None:
        return HttpResponseBadRequest("invalid json")
    exercise = get_object_or_404(
        Exercise.objects.select_related("lesson"), pk=data.get("exercise"), lesson__slug=slug
    )
    if exercise.lesson.is_locked_for(request.user):
        raise Http404
    return check_response(request, exercise, data.get("answer", ""))


@require_POST
def complete_lesson(request, slug):
    data = parse_json(request)
    if data is None or not isinstance(data.get("answers"), dict):
        return HttpResponseBadRequest("invalid json")
    lesson = get_object_or_404(Lesson, slug=slug, is_published=True)
    if lesson.is_locked_for(request.user):
        raise Http404

    # Only the lesson's own exercises count; review questions are practice.
    exercises = list(lesson.exercises.prefetch_related("choices"))
    answers = data["answers"]
    correct = sum(1 for e in exercises if e.is_correct_answer(answers.get(str(e.id), "")))
    score = round(correct * 100 / len(exercises)) if exercises else 100
    passed = score >= PASS_SCORE

    result = {"score": score, "correct": correct, "total": len(exercises), "passed": passed, "xp": 0, "saved": False}
    user = request.user
    if user.is_authenticated:
        with transaction.atomic():
            progress, _ = LessonProgress.objects.select_for_update().get_or_create(user=user, lesson=lesson)
            first_pass = passed and progress.completed_at is None
            progress.attempts += 1
            progress.best_score = max(progress.best_score, score)
            if passed and progress.completed_at is None:
                progress.completed_at = timezone.now()
            progress.save()
            if passed:
                xp = lesson.xp_reward if first_pass else max(1, lesson.xp_reward // 5)
                user.add_xp(xp)
                result["xp"] = xp
        result.update(saved=True, streak=user.current_streak, total_xp=user.xp)
    return JsonResponse(result)


@login_required
def mistakes(request):
    open_mistakes = (
        UserMistake.objects.filter(user=request.user, resolved_at__isnull=True)
        .select_related("exercise__lesson__unit__level")
    )
    batch_ids = list(open_mistakes.order_by("last_wrong_at").values_list("exercise_id", flat=True)[:MISTAKES_BATCH])
    exercises_json = [
        serialize_exercise(e, review_of=e.lesson.title)
        for e in Exercise.objects.filter(pk__in=batch_ids).select_related("lesson").prefetch_related("choices")
    ]
    context = {
        "open_count": open_mistakes.count(),
        "fixed_count": UserMistake.objects.filter(user=request.user, resolved_at__isnull=False).count(),
        "by_lesson": open_mistakes.values("exercise__lesson__title", "exercise__lesson__slug")
        .annotate(n=Count("id"))
        .order_by("-n")[:8],
        "exercises_json": exercises_json,
        "complete_url": reverse("courses:mistakes_complete"),
        "intro_text": f"{len(exercises_json)} задачи, в които сгреши преди. Всяка поправена грешка носи {MISTAKE_XP} XP.",
        "done_url": reverse("accounts:dashboard"),
        "done_label": "Към таблото",
    }
    return render(request, "courses/mistakes.html", context)


@require_POST
@login_required
def complete_mistakes(request):
    data = parse_json(request)
    if data is None or not isinstance(data.get("answers"), dict):
        return HttpResponseBadRequest("invalid json")
    ids = [int(k) for k in data["answers"] if str(k).isdigit()]
    rows = UserMistake.objects.filter(user=request.user, exercise_id__in=ids).select_related("exercise")
    correct = 0
    newly_fixed = []
    for m in rows:
        if m.exercise.is_correct_answer(data["answers"].get(str(m.exercise_id), "")):
            correct += 1
            if m.resolved_at and not m.xp_awarded:
                newly_fixed.append(m.pk)
    total = len(rows)
    xp = MISTAKE_XP * len(newly_fixed)
    if newly_fixed:
        UserMistake.objects.filter(pk__in=newly_fixed).update(xp_awarded=True)
        request.user.add_xp(xp)
    score = round(correct * 100 / total) if total else 100
    return JsonResponse({
        "score": score, "correct": correct, "total": total, "passed": score >= PASS_SCORE,
        "xp": xp, "saved": True, "streak": request.user.current_streak, "total_xp": request.user.xp,
    })
