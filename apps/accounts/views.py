from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.shortcuts import redirect, render

from apps.courses.models import Lesson, LessonProgress, Level
from apps.vocabulary.models import Topic

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
    }
    return render(request, "accounts/dashboard.html", context)


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
