from io import StringIO

from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse

from apps.accounts.models import User
from apps.courses.models import Lesson
from apps.placement.models import PlacementQuestion
from apps.vocabulary.models import Topic


class PageSmokeTests(TestCase):
    """Every public page renders with the seeded starter content."""

    @classmethod
    def setUpTestData(cls):
        call_command("seed_content", stdout=StringIO())

    def assert_ok(self, url):
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200, url)
        return response

    def test_public_pages(self):
        for name in ["core:home", "courses:levels", "vocabulary:topics", "vocabulary:travel", "placement:test",
                     "accounts:login", "accounts:signup"]:
            self.assert_ok(reverse(name))
        for code in ["a1", "b2"]:
            self.assert_ok(reverse("courses:level", args=[code]))
        for lesson in Lesson.objects.all():
            self.assert_ok(lesson.get_absolute_url())
        for topic in Topic.objects.all():
            self.assert_ok(topic.get_absolute_url())

    def test_logged_in_pages(self):
        user = User.objects.create_user("ana@example.com", "pass", display_name="Ана")
        self.client.force_login(user)
        self.assertContains(self.assert_ok(reverse("accounts:dashboard")), "Ана")
        self.assert_ok(reverse("accounts:profile"))
        self.assertRedirects(self.client.get(reverse("core:home")), reverse("accounts:dashboard"))

    def test_placement_flow_for_anonymous(self):
        data = {}
        for q in PlacementQuestion.objects.prefetch_related("choices"):
            data[f"q{q.id}"] = str(next(c.id for c in q.choices.all() if c.is_correct))
        response = self.client.post(reverse("placement:test"), data)
        self.assertRedirects(response, reverse("placement:result"))
        self.assertEqual(self.client.session["placement_level"], "C2")
        self.assertContains(self.client.get(reverse("placement:result")), "C2")

    def test_trust_pages(self):
        for name in ["core:about", "core:faq", "core:privacy", "core:terms"]:
            self.assert_ok(reverse(name))
        with self.settings(CONTACT_EMAIL="hello@example.com"):
            self.assertContains(self.client.get(reverse("core:privacy")), "hello@example.com")
        self.assertNotContains(self.client.get(reverse("core:privacy")), "mailto:")

    def test_level_page_shows_can_do_goals(self):
        self.assertContains(self.client.get(reverse("courses:level", args=["a1"])), "След ниво A1 ще можеш")

    def test_home_shows_real_stats(self):
        response = self.client.get(reverse("core:home"))
        self.assertEqual(response.context["stats"]["lessons"], Lesson.objects.filter(is_published=True).count())

    def test_seo_endpoints(self):
        self.assertContains(self.client.get("/robots.txt"), "Sitemap: http://testserver/sitemap.xml")
        response = self.client.get("/sitemap.xml")
        self.assertContains(response, "/courses/lesson/a1-greetings/")
        self.assertEqual(self.client.get("/does-not-exist/").status_code, 404)

    def test_seed_keeps_saved_words(self):
        from apps.vocabulary.models import SavedWord, Word

        user = User.objects.create_user("keep@example.com", "pass")
        SavedWord.objects.create(user=user, word=Word.objects.first())
        call_command("seed_content", stdout=StringIO())
        self.assertEqual(SavedWord.objects.filter(user=user).count(), 1)

    def test_seed_keeps_mistakes(self):
        from apps.courses.models import Exercise, UserMistake

        user = User.objects.create_user("mist@example.com", "pass")
        UserMistake.objects.create(user=user, exercise=Exercise.objects.first())
        call_command("seed_content", stdout=StringIO())
        self.assertEqual(UserMistake.objects.filter(user=user).count(), 1)

    def test_lessons_show_common_mistakes(self):
        self.assertContains(self.client.get("/courses/lesson/b1-first-conditional/"), "If it will rain")

    def test_seed_is_idempotent(self):
        before = (Lesson.objects.count(), Topic.objects.count(), PlacementQuestion.objects.count())
        call_command("seed_content", stdout=StringIO())
        self.assertEqual(before, (Lesson.objects.count(), Topic.objects.count(), PlacementQuestion.objects.count()))
