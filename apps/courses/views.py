import json

from django.db import transaction
from django.db.models import Count, Prefetch, Q
from django.http import Http404, HttpResponseBadRequest, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views.decorators.http import require_POST

from .models import Choice, Exercise, Lesson, LessonProgress, Level

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


def serialize_exercise(exercise):
    data = {
        "id": exercise.id,
        "type": exercise.type,
        "instruction": exercise.instruction or exercise.get_type_display(),
        "prompt": exercise.prompt,
        "audio": exercise.audio_text,
    }
    if exercise.type == Exercise.Type.CHOICE:
        data["choices"] = [{"id": c.id, "text": c.text} for c in exercise.choices.all()]
    return data


def lesson_detail(request, slug):
    lesson = get_object_or_404(
        Lesson.objects.select_related("unit__level").filter(is_published=True), slug=slug
    )
    if lesson.is_locked_for(request.user):
        return render(request, "courses/lesson_locked.html", {"lesson": lesson})

    exercises = lesson.exercises.prefetch_related("choices")
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

    context = {
        "lesson": lesson,
        "exercises_json": [serialize_exercise(e) for e in exercises],
        "dialogue": lesson.dialogue_lines(),
        "exercise_count": len(exercises),
        "next_lesson": next_lesson,
        "progress": progress,
        "position": index + 1,
        "unit_size": len(siblings),
    }
    return render(request, "courses/lesson_detail.html", context)


def parse_json(request):
    try:
        return json.loads(request.body or b"{}")
    except (ValueError, UnicodeDecodeError):
        return None


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
    correct = exercise.is_correct_answer(data.get("answer", ""))
    response = {"correct": correct, "explanation": exercise.explanation}
    if exercise.type == Exercise.Type.CHOICE:
        response["correct_choice"] = (
            Choice.objects.filter(exercise=exercise, is_correct=True).values_list("id", flat=True).first()
        )
    response["correct_answer"] = (exercise.accepted_answers() or [""])[0]
    return JsonResponse(response)


@require_POST
def complete_lesson(request, slug):
    data = parse_json(request)
    if data is None or not isinstance(data.get("answers"), dict):
        return HttpResponseBadRequest("invalid json")
    lesson = get_object_or_404(Lesson, slug=slug, is_published=True)
    if lesson.is_locked_for(request.user):
        raise Http404

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
