from django.db.models import Count
from django.shortcuts import get_object_or_404, render

from .models import Topic


def topic_list(request):
    topics = Topic.objects.filter(is_travel=False).annotate(word_count=Count("words"))
    return render(request, "vocabulary/topic_list.html", {"topics": topics})


def travel(request):
    topics = Topic.objects.filter(is_travel=True).annotate(word_count=Count("words"))
    return render(request, "vocabulary/travel.html", {"topics": topics})


def topic_detail(request, slug):
    topic = get_object_or_404(Topic, slug=slug)
    locked = topic.is_premium and not (request.user.is_authenticated and request.user.is_premium)
    words = [] if locked else list(topic.words.all())
    cards = [
        {"en": w.english, "bg": w.bulgarian, "ipa": w.transcription, "exEn": w.example_en, "exBg": w.example_bg}
        for w in words
    ]
    others = Topic.objects.filter(is_travel=topic.is_travel).exclude(pk=topic.pk)[:6]
    return render(
        request,
        "vocabulary/topic_detail.html",
        {"topic": topic, "words": words, "cards": cards, "locked": locked, "others": others},
    )
