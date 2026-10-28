import random

from django.core.management.base import BaseCommand
from django.db import transaction

from apps.core.seed import (
    batch5, batch6, batch7, batch8, courses, courses_advanced, courses_extra, courses_more, courses_skills, listening, mistakes, more_audio, more_skills,
    placement, speaking_writing,
    pronunciation, vocabulary, vocabulary_more, writing_tasks,
)
from apps.courses.models import Choice, Exercise, Lesson, Level, Unit
from apps.placement.models import PlacementChoice, PlacementQuestion
from apps.vocabulary.models import Topic, Word

TOPIC_COLORS = {
    "airport": "sky", "hotel": "violet", "restaurant": "amber", "directions-transport": "emerald",
    "shopping": "rose", "emergencies": "orange", "numbers": "indigo", "family": "rose",
    "food-drinks": "emerald", "time-calendar": "sky", **vocabulary_more.COLORS,
}


def outline_headings(html):
    """Theory sits under the page h1, so its headings start at h2 (seed files write h3/h4)."""
    for old, new in (("h3", "h2"), ("h4", "h3")):
        html = html.replace(f"<{old}>", f"<{new}>").replace(f"</{old}>", f"</{new}>")
    return html


def shuffled_choices(prompt, choices, correct):
    """Shuffle choices the same way every run, so the right answer isn't always first."""
    items = [(text, i == correct) for i, text in enumerate(choices)]
    random.Random(prompt).shuffle(items)
    return items


EXERCISE_FIELDS = ["type", "instruction", "prompt", "audio_text", "answers", "explanation"]


class Command(BaseCommand):
    help = "Load starter content (levels, lessons, vocabulary, placement test). Safe to run repeatedly."

    # Each unit, the vocabulary and the placement test commit separately: a dropped connection on a long remote
    # seed keeps what was saved, and running the command again finishes the rest.
    def handle(self, *args, **options):
        self.seed_courses()
        with transaction.atomic():
            self.seed_vocabulary()
        with transaction.atomic():
            self.seed_placement()
        self.stdout.write(self.style.SUCCESS("Starter content loaded."))

    def seed_courses(self):
        levels = {}
        for data in courses.LEVELS:
            level, _ = Level.objects.update_or_create(code=data["code"], defaults={k: v for k, v in data.items() if k != "code"})
            levels[level.code] = level

        units = (courses.UNITS + courses_advanced.UNITS + courses_more.UNITS + courses_extra.UNITS + courses_skills.UNITS
                 + pronunciation.UNITS + more_audio.UNITS + speaking_writing.UNITS + listening.UNITS)
        # Extra lessons for units defined elsewhere, appended after that unit's own lessons (in this order).
        extras = [more_audio.EXTRA_LESSONS, more_skills.EXTRA_LESSONS, batch5.EXTRA_LESSONS, batch6.EXTRA_LESSONS, batch7.EXTRA_LESSONS, batch8.EXTRA_LESSONS]
        units = [{**u, "lessons": u["lessons"] + [l for e in extras for l in e.get(u["slug"], [])]} for u in units]
        all_mistakes = {**mistakes.MISTAKES, **courses_more.MISTAKES, **courses_extra.MISTAKES,
                        **courses_skills.MISTAKES, **more_skills.MISTAKES, **speaking_writing.MISTAKES, **batch5.MISTAKES, **batch6.MISTAKES, **batch7.MISTAKES, **batch8.MISTAKES}
        lesson_count = 0
        for u in units:
            with transaction.atomic():
                unit, _ = Unit.objects.update_or_create(
                    slug=u["slug"],
                    defaults={"level": levels[u["level"]], "title": u["title"], "icon": u["icon"],
                              "order": u["order"], "summary": u.get("summary", "")},
                )
                for order, l in enumerate(u["lessons"], start=1):
                    lesson, _ = Lesson.objects.update_or_create(
                        slug=l["slug"],
                        defaults={"unit": unit, "title": l["title"], "title_en": l.get("title_en", ""), "kind": l["kind"],
                                  "summary": l.get("summary", ""), "theory": outline_headings(l["theory"].strip()),
                                  "order": order, "minutes": l.get("minutes", 5), "xp_reward": l.get("xp", 10),
                                  "dialogue": l.get("dialogue", ""),
                                  "mistakes": "\n".join(" | ".join(m) for m in all_mistakes.get(l["slug"], []))},
                    )
                    tasks = [writing_tasks.TASKS[l["slug"]]] if l["slug"] in writing_tasks.TASKS else []
                    self.seed_exercises(lesson, l["exercises"] + tasks)
                    lesson_count += 1
        self.stdout.write(f"  {len(levels)} levels, {len(units)} units, {lesson_count} lessons")

    def seed_exercises(self, lesson, items):
        """Exercises are updated in place by position, so learners' mistakes linked to them survive.

        Saved with bulk queries (a handful per lesson, not several per exercise) to keep remote seeds short.
        """
        existing = {ex.order: ex for ex in lesson.exercises.all()}
        new, changed = [], []
        for order, e in enumerate(items, start=1):
            values = {"type": e["type"], "instruction": e["instruction"], "prompt": e["prompt"],
                      "audio_text": e.get("audio", ""), "answers": e.get("answers", ""),
                      "explanation": e.get("explanation", "")}
            exercise = existing.get(order)
            if exercise is None:
                new.append(Exercise(lesson=lesson, order=order, **values))
            else:
                for field, value in values.items():
                    setattr(exercise, field, value)
                changed.append(exercise)
        lesson.exercises.filter(order__gt=len(items)).delete()
        Exercise.objects.bulk_create(new)
        Exercise.objects.bulk_update(changed, EXERCISE_FIELDS)
        by_order = {ex.order: ex for ex in new + changed}
        Choice.objects.filter(exercise__lesson=lesson).delete()
        Choice.objects.bulk_create(
            Choice(exercise=by_order[order], text=text, is_correct=ok)
            for order, e in enumerate(items, start=1) if e.get("choices")
            for text, ok in shuffled_choices(e["prompt"] + e.get("audio", ""), e["choices"], e["correct"])
        )

    def seed_vocabulary(self):
        word_count = 0
        topics = vocabulary.TOPICS + vocabulary_more.TOPICS
        for t in topics:
            topic, _ = Topic.objects.update_or_create(
                slug=t["slug"],
                defaults={"title": t["title"], "title_en": t["title_en"], "icon": t["icon"], "level": t["level"],
                          "is_travel": t.get("is_travel", False), "order": t["order"], "summary": t.get("summary", ""),
                          "color": TOPIC_COLORS.get(t["slug"], "teal")},
            )
            # Update words in place (matched by English text) so learners' saved words survive a reseed.
            keep = []
            for i, (en, bg, ipa, ex_en, ex_bg) in enumerate(t["words"], start=1):
                word, _ = Word.objects.update_or_create(
                    topic=topic, english=en,
                    defaults={"bulgarian": bg, "transcription": ipa, "example_en": ex_en, "example_bg": ex_bg, "order": i},
                )
                keep.append(word.pk)
            topic.words.exclude(pk__in=keep).delete()
            word_count += len(t["words"])
        self.stdout.write(f"  {len(topics)} topics, {word_count} words")

    def seed_placement(self):
        PlacementQuestion.objects.all().delete()
        for order, (level, prompt, choices, correct) in enumerate(placement.QUESTIONS, start=1):
            q = PlacementQuestion.objects.create(level=level, prompt=prompt, order=order)
            PlacementChoice.objects.bulk_create(
                PlacementChoice(question=q, text=text, is_correct=i == correct) for i, text in enumerate(choices)
            )
        self.stdout.write(f"  {len(placement.QUESTIONS)} placement questions")
