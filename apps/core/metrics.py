"""Learning metrics for the staff page: do learners start lessons, finish them, come back and improve?

Aggregates only, computed from data the site already stores; nothing is sent to third parties.
"""

from datetime import timedelta

from django.contrib.auth import get_user_model
from django.db.models import Count, Q, Sum
from django.db.models.functions import TruncDate
from django.utils import timezone

from apps.accounts.models import XPEvent
from apps.courses.categories import all_categories
from apps.courses.models import Exercise, Lesson, LessonProgress, UserMistake
from apps.vocabulary.models import SavedWord

MIN_STARTS = 3
TOP_ROWS = 10
RETURN_AFTER_DAYS = 7


def percent(part, whole):
    return round(part * 100 / whole) if whole else None


def learning_metrics():
    now = timezone.now()
    today = timezone.localdate()
    learners = get_user_model().objects.filter(is_staff=False)
    progress = LessonProgress.objects.filter(user__is_staff=False)
    completed = progress.filter(completed_at__isnull=False)

    # Return rate: of learners who joined at least a week ago, how many were active on two or more days.
    cohort = learners.filter(date_joined__lte=now - timedelta(days=RETURN_AFTER_DAYS))
    returning = (
        XPEvent.objects.filter(user__in=cohort)
        .annotate(day=TruncDate("created_at"))
        .values("user")
        .annotate(days=Count("day", distinct=True))
        .filter(days__gte=2)
        .count()
    )

    started_count = progress.count()
    completed_count = completed.count()
    attempts = completed.aggregate(total=Sum("attempts"))["total"] or 0

    # Lessons where learners give up: many starts, few completions.
    lessons = (
        Lesson.objects.filter(is_published=True)
        .annotate(
            starts=Count("progress", filter=Q(progress__user__is_staff=False)),
            completions=Count("progress", filter=Q(progress__user__is_staff=False, progress__completed_at__isnull=False)),
        )
        .filter(starts__gte=MIN_STARTS)
        .select_related("unit__level")
    )
    drop_off = sorted(
        ({"lesson": lesson, "starts": lesson.starts, "completions": lesson.completions,
          "rate": percent(lesson.completions, lesson.starts)} for lesson in lessons),
        key=lambda row: (row["rate"], -row["starts"]),
    )[:TOP_ROWS]

    hardest = (
        Exercise.objects.annotate(learners=Count("mistakes", filter=Q(mistakes__user__is_staff=False)))
        .filter(learners__gt=0)
        .select_related("lesson")
        .order_by("-learners")[:TOP_ROWS]
    )

    mistakes = UserMistake.objects.filter(user__is_staff=False)
    mistakes_total = mistakes.count()
    words = SavedWord.objects.filter(user__is_staff=False)
    word_totals = words.aggregate(reviews=Sum("reviews"), correct=Sum("correct"))

    by_kind = dict(completed.values("lesson__kind").annotate(n=Count("id")).values_list("lesson__kind", "n"))
    categories = [{**cat, "completed": sum(by_kind.get(kind, 0) for kind in cat["kinds"])} for cat in all_categories()]

    learner_count = learners.count()
    active_learners = progress.values("user").distinct().count()
    return {
        "learners": learner_count,
        "new_learners": learners.filter(date_joined__gte=now - timedelta(days=30)).count(),
        "active_week": learners.filter(last_activity_date__gte=today - timedelta(days=6)).count(),
        "activation_rate": percent(active_learners, learner_count),
        "cohort": cohort.count(),
        "return_rate": percent(returning, cohort.count()),
        "started": started_count,
        "completed": completed_count,
        "completion_rate": percent(completed_count, started_count),
        "attempts_per_pass": round(attempts / completed_count, 1) if completed_count else None,
        "drop_off": drop_off,
        "min_starts": MIN_STARTS,
        "hardest": hardest,
        "mistakes_total": mistakes_total,
        "mistakes_fixed_rate": percent(mistakes.filter(resolved_at__isnull=False).count(), mistakes_total),
        "word_reviews": word_totals["reviews"] or 0,
        "word_accuracy": percent(word_totals["correct"] or 0, word_totals["reviews"] or 0),
        "words_saved": words.count(),
        "words_mastered": words.filter(box__gte=SavedWord.MAX_BOX).count(),
        "categories": categories,
    }
