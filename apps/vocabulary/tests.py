import json
from datetime import timedelta

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from apps.accounts.models import User

from .models import SavedWord, Topic, Word


class SavedWordTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.topic = Topic.objects.create(title="Хотел", title_en="Hotel", slug="hotel")
        cls.words = [Word.objects.create(topic=cls.topic, english=f"word {i}", bulgarian=f"дума {i}") for i in range(3)]

    def setUp(self):
        self.user = User.objects.create_user("ana@example.com", "pass")
        self.client.force_login(self.user)

    def post(self, name, *args, payload=None):
        return self.client.post(reverse(name, args=args), data=json.dumps(payload or {}), content_type="application/json")

    def test_toggle_saves_and_unsaves(self):
        self.assertTrue(self.post("vocabulary:toggle_saved", self.words[0].id).json()["saved"])
        self.assertFalse(self.post("vocabulary:toggle_saved", self.words[0].id).json()["saved"])
        self.assertFalse(SavedWord.objects.exists())

    def test_save_topic_adds_missing_words_once(self):
        SavedWord.objects.create(user=self.user, word=self.words[0])
        self.assertEqual(self.post("vocabulary:save_topic", "hotel").json()["deck_size"], 3)
        self.assertEqual(self.post("vocabulary:save_topic", "hotel").json()["deck_size"], 3)

    def test_anonymous_cannot_save(self):
        self.client.logout()
        self.assertEqual(self.post("vocabulary:toggle_saved", self.words[0].id).status_code, 401)

    def test_leitner_schedule(self):
        saved = SavedWord.objects.create(user=self.user, word=self.words[0])
        today = timezone.localdate()
        self.assertTrue(saved.record(True))
        self.assertEqual((saved.box, saved.due_date), (2, today + timedelta(days=3)))
        # Not due any more: a correct answer doesn't move it up again.
        self.assertFalse(saved.record(True))
        self.assertEqual(saved.box, 2)
        saved.record(False)
        self.assertEqual((saved.box, saved.due_date), (1, today))

    def test_review_awards_xp_only_for_due_known_words(self):
        saved = SavedWord.objects.create(user=self.user, word=self.words[0])
        first = self.post("vocabulary:review_answer", saved.id, payload={"knew": True}).json()
        again = self.post("vocabulary:review_answer", saved.id, payload={"knew": True}).json()
        self.assertEqual((first["xp"], again["xp"]), (1, 0))
        self.user.refresh_from_db()
        self.assertEqual(self.user.xp, 1)

    def test_review_answer_only_for_own_words(self):
        other = User.objects.create_user("b@example.com", "pass")
        saved = SavedWord.objects.create(user=other, word=self.words[0])
        self.assertEqual(self.post("vocabulary:review_answer", saved.id, payload={"knew": True}).status_code, 404)

    def test_pages(self):
        SavedWord.objects.create(user=self.user, word=self.words[0])
        self.assertContains(self.client.get(reverse("vocabulary:my_words")), "word 0")
        self.assertContains(self.client.get(reverse("vocabulary:review")), "review-data")
        self.assertContains(self.client.get(self.topic.get_absolute_url()), 'aria-pressed="true"')
