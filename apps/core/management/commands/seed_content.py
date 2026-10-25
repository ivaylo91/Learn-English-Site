from django.core.management.base import BaseCommand
from django.db import transaction

from apps.core.seed import courses, placement, vocabulary
from apps.courses.models import Choice, Exercise, Lesson, Level, Unit
from apps.placement.models import PlacementChoice, PlacementQuestion
from apps.vocabulary.models import Topic, Word


class Command(BaseCommand):
    help = "Load starter content (levels, lessons, vocabulary, placement test). Safe to run repeatedly."

    @transaction.atomic
    def handle(self, *args, **options):
        self.seed_courses()
        self.seed_vocabulary()
        self.seed_placement()
        self.stdout.write(self.style.SUCCESS("Starter content loaded."))

    def seed_courses(self):
        levels = {}
        for data in courses.LEVELS:
            level, _ = Level.objects.update_or_create(code=data["code"], defaults={k: v for k, v in data.items() if k != "code"})
            levels[level.code] = level

        lesson_count = 0
        for u in courses.UNITS:
            unit, _ = Unit.objects.update_or_create(
                slug=u["slug"],
                defaults={"level": levels[u["level"]], "title": u["title"], "icon": u["icon"],
                          "order": u["order"], "summary": u.get("summary", "")},
            )
            for order, l in enumerate(u["lessons"], start=1):
                lesson, _ = Lesson.objects.update_or_create(
                    slug=l["slug"],
                    defaults={"unit": unit, "title": l["title"], "title_en": l.get("title_en", ""), "kind": l["kind"],
                              "summary": l.get("summary", ""), "theory": l["theory"].strip(), "order": order,
                              "minutes": l.get("minutes", 5), "xp_reward": l.get("xp", 10)},
                )
                # Exercises are replaced wholesale so edits in the seed file take effect.
                lesson.exercises.all().delete()
                for ex_order, e in enumerate(l["exercises"], start=1):
                    exercise = Exercise.objects.create(
                        lesson=lesson, type=e["type"], instruction=e["instruction"], prompt=e["prompt"],
                        answers=e.get("answers", ""), explanation=e.get("explanation", ""), order=ex_order,
                    )
                    for i, text in enumerate(e.get("choices", [])):
                        Choice.objects.create(exercise=exercise, text=text, is_correct=i == e["correct"])
                lesson_count += 1
        self.stdout.write(f"  {len(levels)} levels, {len(courses.UNITS)} units, {lesson_count} lessons")

    def seed_vocabulary(self):
        word_count = 0
        for t in vocabulary.TOPICS:
            topic, _ = Topic.objects.update_or_create(
                slug=t["slug"],
                defaults={"title": t["title"], "title_en": t["title_en"], "icon": t["icon"], "level": t["level"],
                          "is_travel": t.get("is_travel", False), "order": t["order"], "summary": t.get("summary", "")},
            )
            topic.words.all().delete()
            Word.objects.bulk_create(
                Word(topic=topic, english=en, bulgarian=bg, transcription=ipa, example_en=ex_en, example_bg=ex_bg, order=i)
                for i, (en, bg, ipa, ex_en, ex_bg) in enumerate(t["words"], start=1)
            )
            word_count += len(t["words"])
        self.stdout.write(f"  {len(vocabulary.TOPICS)} topics, {word_count} words")

    def seed_placement(self):
        PlacementQuestion.objects.all().delete()
        for order, (level, prompt, choices, correct) in enumerate(placement.QUESTIONS, start=1):
            q = PlacementQuestion.objects.create(level=level, prompt=prompt, order=order)
            PlacementChoice.objects.bulk_create(
                PlacementChoice(question=q, text=text, is_correct=i == correct) for i, text in enumerate(choices)
            )
        self.stdout.write(f"  {len(placement.QUESTIONS)} placement questions")
