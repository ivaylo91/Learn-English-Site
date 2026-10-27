from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.shortcuts import redirect, render
from django.utils import timezone

from apps.courses.models import Lesson, LessonProgress, Level, UserMistake
from apps.courses.views import category_counts
from apps.vocabulary.models import SavedWord, Topic

from .achievements import achievements_for, week_start, weekly_leaderboard
from .forms import ProfileForm, SignupForm


def signup(request):
    if request.user.is_authenticated:
        return redirect("accounts:dashboard")
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # Keep the result of a placement test taken before registering.
            user.level = request.session.pop("placement_level", "") or user.level
            user.save()
            login(request, user)
            messages.success(request, f"Здравей, {user.name}! Нека настроим профила ти.")
            return redirect("accounts:profile")
    else:
        form = SignupForm()
    return render(request, "accounts/signup.html", {"form": form})


def next_lesson_for(user):
    completed = LessonProgress.objects.filter(user=user, completed_at__isnull=False).values("lesson_id")
    lessons = Lesson.objects.filter(is_published=True).exclude(id__in=completed).select_related("unit__level")
    if user.level:
        at_level = lessons.filter(unit__level__code=user.level).first()
        if at_level:
            return at_level
    return lessons.first()


@login_required
def dashboard(request):
    user = request.user
    completed_ids = set(
        LessonProgress.objects.filter(user=user, completed_at__isnull=False).values_list("lesson_id", flat=True)
    )
    levels = Level.objects.annotate(
        total=Count("units__lessons", filter=Q(units__lessons__is_published=True))
    ).order_by("order")
    level_rows = []
    for level in levels:
        done = Lesson.objects.filter(unit__level=level, id__in=completed_ids).count()
        level_rows.append({"level": level, "done": done, "total": level.total})

    xp_today = user.xp_today()
    recent = (
        LessonProgress.objects.filter(user=user, completed_at__isnull=False)
        .select_related("lesson__unit__level")
        .order_by("-updated_at")[:5]
    )
    context = {
        "next_lesson": next_lesson_for(user),
        "level_rows": level_rows,
        "xp_today": xp_today,
        "goal_percent": min(100, round(xp_today * 100 / user.daily_goal_xp)) if user.daily_goal_xp else 0,
        "completed_count": len(completed_ids),
        "recent": recent,
        "travel_topics": Topic.objects.filter(is_travel=True)[:4],
        "due_words": SavedWord.objects.filter(user=user, due_date__lte=timezone.localdate()).count(),
        "deck_size": SavedWord.objects.filter(user=user).count(),
        "open_mistakes": UserMistake.objects.filter(user=user, resolved_at__isnull=True).count(),
        "achievements": achievements_for(user),
        "categories": category_counts(list(Lesson.objects.filter(is_published=True).only("id", "kind")), completed_ids),
    }
    context["earned_count"] = sum(1 for a in context["achievements"] if a["earned"])
    return render(request, "accounts/dashboard.html", context)


def leaderboard(request):
    leaders = list(weekly_leaderboard())
    my_rank = None
    if request.user.is_authenticated:
        my_rank = next((i for i, u in enumerate(leaders, start=1) if u.pk == request.user.pk), None)
    return render(request, "accounts/leaderboard.html", {"leaders": leaders, "week_start": week_start(), "my_rank": my_rank})


@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Профилът е запазен.")
            if not form.cleaned_data["level"]:
                return redirect("placement:test")
            return redirect("accounts:dashboard")
    else:
        form = ProfileForm(instance=request.user)
    return render(request, "accounts/profile.html", {"form": form})


@login_required
def delete_account(request):
    """GDPR erasure: delete the user and everything linked to them (progress, words, mistakes)."""
    if request.method == "POST":
        if request.POST.get("confirm_email", "").strip().lower() != request.user.email.lower():
            messages.error(request, "Имейлът не съвпада. Профилът не е изтрит.")
            return redirect("accounts:profile")
        user = request.user
        logout(request)
        user.delete()
        messages.success(request, "Профилът и всички данни са изтрити.")
        return redirect("core:home")
    return redirect("accounts:profile")
