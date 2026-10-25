from django.shortcuts import redirect, render

from apps.courses.models import Level
from apps.vocabulary.models import Topic


def home(request):
    if request.user.is_authenticated and request.GET.get("landing") is None:
        return redirect("accounts:dashboard")
    context = {
        "levels": Level.objects.all(),
        "travel_topics": Topic.objects.filter(is_travel=True)[:6],
    }
    return render(request, "core/home.html", context)
