import json

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from apps.accounts.models import User

from .models import Choice, Exercise, Lesson, LessonProgress, Level, Unit, normalize_answer


class ContentMixin:
    @classmethod
    def setUpTestData(cls):
        level = Level.objects.create(code="A1", title="Начинаещи", summary="s", order=1)
        unit = Unit.objects.create(level=level, title="U", slug="u", order=1)
        cls.lesson = Lesson.objects.create(unit=unit, title="To be", slug="to-be", xp_reward=10)
        cls.choice_ex = Exercise.objects.create(lesson=cls.lesson, type="choice", prompt="I ___ a teacher.", order=1)
        cls.right = Choice.objects.create(exercise=cls.choice_ex, text="am", is_correct=True)
        cls.wrong = Choice.objects.create(exercise=cls.choice_ex, text="is")
        cls.fill_ex = Exercise.objects.create(
            lesson=cls.lesson, type="fill", prompt="We ___ here.", answers="are|'re", order=2
        )
        cls.tr_ex = Exercise.objects.create(
            lesson=cls.lesson, type="translate", prompt="Аз съм от България.",
            answers="I am from Bulgaria|I'm from Bulgaria", order=3,
        )

    def post_json(self, name, payload):
        return self.client.post(
            reverse(name, args=[self.lesson.slug]), data=json.dumps(payload), content_type="application/json"
        )

    def complete(self, answers):
        return self.post_json("courses:complete", {"answers": answers}).json()

    def all_correct(self):
        return {
            str(self.choice_ex.id): str(self.right.id),
            str(self.fill_ex.id): "are",
            str(self.tr_ex.id): "I'm from Bulgaria.",
        }


class AnswerCheckingTests(ContentMixin, TestCase):
    def test_normalize(self):
        self.assertEqual(normalize_answer("  I’m  from Bulgaria! "), "i'm from bulgaria")

    def test_choice_by_id(self):
        self.assertTrue(self.choice_ex.is_correct_answer(str(self.right.id)))
        self.assertFalse(self.choice_ex.is_correct_answer(str(self.wrong.id)))
        self.assertFalse(self.choice_ex.is_correct_answer("am"))

    def test_text_variants(self):
        self.assertTrue(self.tr_ex.is_correct_answer("i am from bulgaria"))
        self.assertTrue(self.tr_ex.is_correct_answer("I’m from Bulgaria."))
        self.assertFalse(self.tr_ex.is_correct_answer("I from Bulgaria"))

    def test_check_endpoint(self):
        response = self.post_json("courses:check", {"exercise": self.choice_ex.id, "answer": str(self.wrong.id)}).json()
        self.assertFalse(response["correct"])
        self.assertEqual(response["correct_choice"], self.right.id)

    def test_check_rejects_exercise_from_other_lesson(self):
        other = Lesson.objects.create(unit=self.lesson.unit, title="X", slug="x")
        response = self.client.post(
            reverse("courses:check", args=[other.slug]),
            data=json.dumps({"exercise": self.choice_ex.id, "answer": "1"}), content_type="application/json",
        )
        self.assertEqual(response.status_code, 404)


class CompleteLessonTests(ContentMixin, TestCase):
    def setUp(self):
        self.user = User.objects.create_user("ana@example.com", "pass")

    def test_anonymous_gets_score_but_nothing_saved(self):
        result = self.complete(self.all_correct())
        self.assertEqual((result["score"], result["passed"], result["saved"]), (100, True, False))
        self.assertFalse(LessonProgress.objects.exists())

    def test_first_pass_awards_full_xp_then_reduced(self):
        self.client.force_login(self.user)
        first = self.complete(self.all_correct())
        second = self.complete(self.all_correct())
        self.assertEqual((first["xp"], second["xp"]), (10, 2))
        self.user.refresh_from_db()
        self.assertEqual(self.user.xp, 12)
        progress = LessonProgress.objects.get(user=self.user)
        self.assertEqual((progress.attempts, progress.best_score), (2, 100))
        self.assertTrue(progress.is_completed)

    def test_failing_gives_no_xp_and_not_completed(self):
        self.client.force_login(self.user)
        result = self.complete({str(self.choice_ex.id): str(self.wrong.id)})
        self.assertEqual((result["score"], result["passed"], result["xp"]), (0, False, 0))
        self.assertFalse(LessonProgress.objects.get(user=self.user).is_completed)

    def test_invalid_payload(self):
        response = self.client.post(
            reverse("courses:complete", args=[self.lesson.slug]), data="nope", content_type="application/json"
        )
        self.assertEqual(response.status_code, 400)

    def test_premium_lesson_locked(self):
        self.lesson.is_premium = True
        self.lesson.save()
        response = self.client.get(self.lesson.get_absolute_url())
        self.assertTemplateUsed(response, "courses/lesson_locked.html")
        self.assertEqual(self.post_json("courses:complete", {"answers": {}}).status_code, 404)


class AudioLessonTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        level = Level.objects.create(code="A1", title="Начинаещи", summary="s", order=1)
        unit = Unit.objects.create(level=level, title="U", slug="u", order=1)
        cls.lesson = Lesson.objects.create(
            unit=unit, title="Café", slug="cafe", kind=Lesson.Kind.LISTENING,
            dialogue="Barista | Hi! | Здравейте!\nMaria | A tea, please. | Един чай.\nBarista | Sure.\nbroken line",
        )
        cls.dictation = Exercise.objects.create(
            lesson=cls.lesson, type="dictation", prompt="Слушай.", audio_text="Have a nice day!"
        )

    def test_dictation_defaults_to_audio_text(self):
        self.assertTrue(self.dictation.is_correct_answer("have a nice day"))
        self.assertFalse(self.dictation.is_correct_answer("have a good day"))

    def test_dialogue_lines(self):
        lines = self.lesson.dialogue_lines()
        self.assertEqual(len(lines), 3)
        self.assertEqual([l["who"] for l in lines], [0, 1, 0])
        self.assertEqual(lines[1], {"speaker": "Maria", "who": 1, "en": "A tea, please.", "bg": "Един чай."})
        self.assertEqual(lines[2]["bg"], "")

    def test_lesson_page_has_player_and_exercise_audio(self):
        response = self.client.get(self.lesson.get_absolute_url())
        self.assertContains(response, "data-dialogue-play")
        self.assertEqual(response.context["exercises_json"][0]["audio"], "Have a nice day!")

    def test_listening_category_groups_audio_kinds(self):
        Lesson.objects.create(unit=self.lesson.unit, title="Grammar", slug="grammar")
        Lesson.objects.create(unit=self.lesson.unit, title="Th", slug="pron", kind=Lesson.Kind.PRONUNCIATION, order=1)
        response = self.client.get(reverse("courses:category", args=["listening"]))
        self.assertEqual(sorted(l.slug for l in response.context["lessons"]), ["cafe", "pron"])

    def test_old_listening_url_redirects(self):
        response = self.client.get(reverse("courses:listening"))
        self.assertRedirects(response, reverse("courses:category", args=["listening"]), status_code=301)


class CategoryTests(TestCase):
    def test_every_kind_has_exactly_one_category(self):
        from .categories import CATEGORIES, KIND_TO_CATEGORY

        self.assertEqual(set(KIND_TO_CATEGORY), {k for k, _ in Lesson.Kind.choices})
        self.assertEqual(list(CATEGORIES), ["listening", "reading", "writing", "grammar", "vocabulary"])

    def test_conversation_lessons_show_as_vocabulary(self):
        lesson = Lesson(kind=Lesson.Kind.CONVERSATION)
        self.assertEqual((lesson.category["key"], lesson.kind_theme["label"]), ("vocabulary", "Речник"))

    def test_unknown_category_404(self):
        self.assertEqual(self.client.get("/courses/category/cooking/").status_code, 404)


class WordOrderTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        level = Level.objects.create(code="A1", title="Начинаещи", summary="s", order=1)
        unit = Unit.objects.create(level=level, title="U", slug="u", order=1)
        lesson = Lesson.objects.create(unit=unit, title="Order", slug="order")
        cls.exercise = Exercise.objects.create(
            lesson=lesson, type="order", prompt="Те не са у дома.", answers="They are not at home|They aren't at home"
        )

    def test_tiles_are_the_answer_words_shuffled(self):
        tiles = self.exercise.word_tiles()
        self.assertEqual(sorted(tiles), sorted("They are not at home".split()))
        self.assertNotEqual(tiles, "They are not at home".split())
        self.assertEqual(tiles, self.exercise.word_tiles())  # stable between requests

    def test_grading(self):
        self.assertTrue(self.exercise.is_correct_answer("They are not at home"))
        self.assertFalse(self.exercise.is_correct_answer("Are they not at home"))


class LearningLoopTests(ContentMixin, TestCase):
    """Mistakes deck, warm-up review questions and common-mistake cards."""

    def setUp(self):
        self.user = User.objects.create_user("loop@example.com", "pass")
        self.client.force_login(self.user)

    def check(self, exercise, answer):
        return self.client.post(
            reverse("courses:check_any"), data=json.dumps({"exercise": exercise.id, "answer": answer}),
            content_type="application/json",
        ).json()

    def test_wrong_answer_is_recorded_and_resolved_later(self):
        from .models import UserMistake

        self.check(self.choice_ex, str(self.wrong.id))
        self.check(self.choice_ex, str(self.wrong.id))
        mistake = UserMistake.objects.get(user=self.user, exercise=self.choice_ex)
        self.assertEqual((mistake.wrong_count, mistake.resolved_at), (2, None))
        self.check(self.choice_ex, str(self.right.id))
        mistake.refresh_from_db()
        self.assertIsNotNone(mistake.resolved_at)

    def test_anonymous_check_records_nothing(self):
        from .models import UserMistake

        self.client.logout()
        self.assertFalse(self.check(self.choice_ex, str(self.wrong.id))["correct"])
        self.assertFalse(UserMistake.objects.exists())

    def test_premium_exercise_not_checkable(self):
        self.lesson.is_premium = True
        self.lesson.save()
        response = self.client.post(
            reverse("courses:check_any"), data=json.dumps({"exercise": self.choice_ex.id, "answer": "1"}),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 404)

    def test_mistakes_practice_awards_xp_once(self):
        self.check(self.fill_ex, "is")  # wrong
        page = self.client.get(reverse("courses:mistakes"))
        self.assertEqual([e["id"] for e in page.context["exercises_json"]], [self.fill_ex.id])
        self.check(self.fill_ex, "are")  # fixed
        payload = json.dumps({"answers": {str(self.fill_ex.id): "are"}})
        url = reverse("courses:mistakes_complete")
        first = self.client.post(url, data=payload, content_type="application/json").json()
        again = self.client.post(url, data=payload, content_type="application/json").json()
        self.assertEqual((first["xp"], again["xp"]), (2, 0))

    def test_review_questions_come_from_finished_lessons(self):
        other = Lesson.objects.create(unit=self.lesson.unit, title="Other", slug="other")
        Exercise.objects.create(lesson=other, type="fill", prompt="x ___", answers="y")
        LessonProgress.objects.create(user=self.user, lesson=self.lesson, completed_at=timezone.now())
        data = self.client.get(other.get_absolute_url()).context["exercises_json"]
        review = [e for e in data if e.get("review")]
        self.assertEqual(len(review), 2)
        self.assertTrue(all(e["review"] == "To be" for e in review))
        # Review answers don't change the lesson score.
        result = self.client.post(
            reverse("courses:complete", args=["other"]),
            data=json.dumps({"answers": {str(self.choice_ex.id): "nope", str(other.exercises.get().id): "y"}}),
            content_type="application/json",
        ).json()
        self.assertEqual((result["score"], result["total"]), (100, 1))

    def test_mistake_cards(self):
        self.lesson.mistakes = "He is doctor. | He is a doctor. | Нужен е член.\nbroken\nA | B"
        self.assertEqual(self.lesson.mistake_cards(), [
            {"wrong": "He is doctor.", "right": "He is a doctor.", "why": "Нужен е член."},
            {"wrong": "A", "right": "B", "why": ""},
        ])


class SpeakingTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        level = Level.objects.create(code="A1", title="Начинаещи", summary="s", order=1)
        unit = Unit.objects.create(level=level, title="U", slug="u", order=1)
        cls.lesson = Lesson.objects.create(unit=unit, title="Speak", slug="speak", kind="speaking")
        cls.speak = Exercise.objects.create(
            lesson=cls.lesson, type="speak", prompt="I live in Sofia.", audio_text="I live in Sofia.", answers="I live in Sofia."
        )

    def test_close_transcripts_pass(self):
        self.assertTrue(self.speak.is_correct_answer("i live in sofia"))
        self.assertTrue(self.speak.is_correct_answer("I live in Sophia"))  # recogniser spelling of the name
        self.assertFalse(self.speak.is_correct_answer("I love"))
        self.assertFalse(self.speak.is_correct_answer("I leave in Sofia"))  # live/leave is the point of the practice
        self.assertFalse(self.speak.is_correct_answer("I live in Sofia tomorrow morning please"))
        self.assertFalse(self.speak.is_correct_answer(""))

    def test_lesson_page_serialises_speak(self):
        data = self.client.get(self.lesson.get_absolute_url()).context["exercises_json"]
        self.assertEqual(data[0]["type"], "speak")
        self.assertEqual(data[0]["audio"], "I live in Sofia.")
