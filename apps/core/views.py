from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_GET

from apps.courses.models import Lesson, Level
from apps.vocabulary.models import Topic


def home(request):
    if request.user.is_authenticated and request.GET.get("landing") is None:
        return redirect("accounts:dashboard")
    context = {
        "levels": Level.objects.all(),
        "travel_topics": Topic.objects.filter(is_travel=True)[:6],
        "listening_lessons": Lesson.objects.filter(is_published=True, kind=Lesson.Kind.LISTENING)
        .select_related("unit__level")[:4],
    }
    return render(request, "core/home.html", context)


@require_GET
def robots_txt(request):
    lines = [
        "User-agent: *",
        "Disallow: /admin/",
        "Disallow: /accounts/",
        "Disallow: /vocabulary/review/",
        "Disallow: /vocabulary/my-words/",
        f"Sitemap: {request.build_absolute_uri(reverse('sitemap'))}",
    ]
    return HttpResponse("\n".join(lines) + "\n", content_type="text/plain")
