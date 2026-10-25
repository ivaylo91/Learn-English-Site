import json

from django.test import TestCase
from django.urls import reverse

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

    def test_listening_page_lists_only_listening(self):
        Lesson.objects.create(unit=self.lesson.unit, title="Grammar", slug="grammar")
        response = self.client.get(reverse("courses:listening"))
        self.assertEqual([l.slug for l in response.context["lessons"]], ["cafe"])
