"""Achievements are computed from the learner's stats, so nothing extra is stored."""

from datetime import timedelta

from django.db.models import Count, Q, Sum
from django.utils import timezone

from apps.core.theme import theme

# (key, title, description, icon, color, test(stats))
ACHIEVEMENTS = [
    ("first-lesson", "Първа стъпка", "Завърши първия си урок.", "fa-shoe-prints", "emerald", lambda s: s["lessons"] >= 1),
    ("five-lessons", "Набираш скорост", "Завърши 5 урока.", "fa-gauge-high", "sky", lambda s: s["lessons"] >= 5),
    ("twenty-lessons", "Неспираем", "Завърши 20 урока.", "fa-rocket", "violet", lambda s: s["lessons"] >= 20),
    ("first-listening", "Отворени уши", "Завърши урок по слушане.", "fa-headphones", "rose", lambda s: s["listening"] >= 1),
    ("streak-3", "Три поредни дни", "Учи 3 дни подред.", "fa-fire", "orange", lambda s: s["streak"] >= 3),
    ("streak-7", "Цяла седмица", "Учи 7 дни подред.", "fa-fire-flame-curved", "orange", lambda s: s["streak"] >= 7),
    ("streak-30", "Месец без почивка", "Учи 30 дни подред.", "fa-crown", "amber", lambda s: s["streak"] >= 30),
    ("xp-100", "Сто точки", "Събери 100 XP.", "fa-bolt", "amber", lambda s: s["xp"] >= 100),
    ("xp-1000", "Хиляда точки", "Събери 1000 XP.", "fa-star", "indigo", lambda s: s["xp"] >= 1000),
    ("words-25", "Колекционер", "Запази 25 думи за преговор.", "fa-box-archive", "teal", lambda s: s["saved"] >= 25),
    ("words-mastered", "Здрава памет", "Научи напълно 10 думи.", "fa-brain", "rose", lambda s: s["mastered"] >= 10),
    ("perfect", "Перфекционист", "Завърши урок със 100%.", "fa-medal", "emerald", lambda s: s["perfect"] >= 1),
]


def user_stats(user):
    from apps.courses.models import Lesson, LessonProgress
    from apps.vocabulary.models import SavedWord

    done = LessonProgress.objects.filter(user=user, completed_at__isnull=False)
    progress = done.aggregate(
        lessons=Count("id"),
        listening=Count("id", filter=Q(lesson__kind=Lesson.Kind.LISTENING)),
        perfect=Count("id", filter=Q(best_score=100)),
    )
    words = SavedWord.objects.filter(user=user).aggregate(
        saved=Count("id"), mastered=Count("id", filter=Q(box__gte=SavedWord.MAX_BOX))
    )
    return {**progress, **words, "xp": user.xp, "streak": max(user.longest_streak, user.current_streak)}


def achievements_for(user):
    stats = user_stats(user)
    return [
        {"key": key, "title": title, "description": desc, "icon": icon, "theme": theme(color), "earned": test(stats)}
        for key, title, desc, icon, color, test in ACHIEVEMENTS
    ]


def week_start():
    today = timezone.localdate()
    return today - timedelta(days=today.weekday())


def weekly_leaderboard(limit=20):
    """Top learners by XP earned since Monday."""
    from .models import User

    return (
        User.objects.filter(is_active=True, show_in_leaderboard=True, xp_events__created_at__date__gte=week_start())
        .annotate(week_xp=Sum("xp_events__amount"))
        .filter(week_xp__gt=0)
        .order_by("-week_xp", "id")[:limit]
    )
