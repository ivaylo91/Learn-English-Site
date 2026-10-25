import json

from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views.decorators.http import require_POST

from .models import SavedWord, Topic, Word

REVIEW_BATCH = 20


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
    saved_ids = set()
    if request.user.is_authenticated:
        saved_ids = set(
            SavedWord.objects.filter(user=request.user, word__topic=topic).values_list("word_id", flat=True)
        )
    others = Topic.objects.filter(is_travel=topic.is_travel).exclude(pk=topic.pk)[:6]
    return render(
        request,
        "vocabulary/topic_detail.html",
        {"topic": topic, "words": words, "cards": cards, "locked": locked, "others": others, "saved_ids": saved_ids},
    )


@require_POST
def toggle_saved(request, word_id):
    if not request.user.is_authenticated:
        return JsonResponse({"error": "login"}, status=401)
    word = get_object_or_404(Word, pk=word_id)
    saved, created = SavedWord.objects.get_or_create(user=request.user, word=word)
    if not created:
        saved.delete()
    return JsonResponse({"saved": created, "deck_size": request.user.saved_words.count()})


@require_POST
def save_topic(request, slug):
    if not request.user.is_authenticated:
        return JsonResponse({"error": "login"}, status=401)
    topic = get_object_or_404(Topic, slug=slug)
    existing = set(SavedWord.objects.filter(user=request.user, word__topic=topic).values_list("word_id", flat=True))
    SavedWord.objects.bulk_create(
        SavedWord(user=request.user, word=w) for w in topic.words.exclude(pk__in=existing)
    )
    return JsonResponse({"saved": True, "deck_size": request.user.saved_words.count()})


@login_required
def my_words(request):
    deck = SavedWord.objects.filter(user=request.user).select_related("word__topic")
    today = timezone.localdate()
    stats = deck.aggregate(
        total=Count("id"),
        due=Count("id", filter=Q(due_date__lte=today)),
        mastered=Count("id", filter=Q(box__gte=SavedWord.MAX_BOX)),
    )
    boxes = [
        {"box": b, "count": sum(1 for s in deck if s.box == b)} for b in range(1, SavedWord.MAX_BOX + 1)
    ]
    return render(request, "vocabulary/my_words.html", {"deck": deck, "stats": stats, "boxes": boxes})


@login_required
def review(request):
    due = (
        SavedWord.objects.filter(user=request.user, due_date__lte=timezone.localdate())
        .select_related("word__topic")
        .order_by("due_date", "box", "?")[:REVIEW_BATCH]
    )
    cards = [
        {"id": s.id, "en": s.word.english, "bg": s.word.bulgarian, "ipa": s.word.transcription,
         "exEn": s.word.example_en, "exBg": s.word.example_bg, "box": s.box, "topic": s.word.topic.title}
        for s in due
    ]
    return render(request, "vocabulary/review.html", {"cards": cards})


@require_POST
@login_required
def review_answer(request, saved_id):
    try:
        knew_it = bool(json.loads(request.body or b"{}").get("knew"))
    except (ValueError, AttributeError):
        return HttpResponseBadRequest("invalid json")
    saved = get_object_or_404(SavedWord, pk=saved_id, user=request.user)
    counted = saved.record(knew_it)
    # One XP per remembered word that was actually due, so repeats can't farm points.
    xp = 1 if (counted and knew_it) else 0
    if xp:
        request.user.add_xp(xp)
    return JsonResponse({"box": saved.box, "due_date": saved.due_date.isoformat(), "xp": xp,
                         "streak": request.user.current_streak})
