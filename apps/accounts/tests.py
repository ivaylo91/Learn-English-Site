from datetime import timedelta

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import User


class StreakTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("ana@example.com", "s3cret-pass!")

    def test_first_activity_starts_streak(self):
        self.user.add_xp(10)
        self.assertEqual((self.user.xp, self.user.current_streak), (10, 1))
        self.assertEqual(self.user.xp_today(), 10)

    def test_same_day_does_not_grow_streak(self):
        self.user.add_xp(10)
        self.user.add_xp(5)
        self.assertEqual((self.user.xp, self.user.current_streak), (15, 1))

    def test_consecutive_day_grows_streak(self):
        self.user.last_activity_date = timezone.localdate() - timedelta(days=1)
        self.user.current_streak = 4
        self.user.save()
        self.user.add_xp(10)
        self.assertEqual(self.user.current_streak, 5)
        self.assertEqual(self.user.longest_streak, 5)

    def test_gap_resets_streak(self):
        self.user.last_activity_date = timezone.localdate() - timedelta(days=3)
        self.user.current_streak = 7
        self.user.longest_streak = 7
        self.user.save()
        self.user.add_xp(10)
        self.assertEqual(self.user.current_streak, 1)
        self.assertEqual(self.user.longest_streak, 7)

    def test_premium_flag(self):
        self.assertFalse(self.user.is_premium)
        self.user.plan = User.Plan.PREMIUM
        self.assertTrue(self.user.is_premium)
        self.user.premium_until = timezone.now() - timedelta(days=1)
        self.assertFalse(self.user.is_premium)


class AuthFlowTests(TestCase):
    def test_signup_logs_in_and_keeps_placement_level(self):
        session = self.client.session
        session["placement_level"] = "B1"
        session.save()
        response = self.client.post(reverse("accounts:signup"), {
            "display_name": "Иво", "email": "ivo@example.com",
            "password1": "Long-enough-pass-42", "password2": "Long-enough-pass-42",
        })
        self.assertRedirects(response, reverse("accounts:profile"))
        user = User.objects.get(email="ivo@example.com")
        self.assertEqual(user.level, "B1")
        self.assertEqual(int(self.client.session["_auth_user_id"]), user.pk)

    def test_login_with_email(self):
        User.objects.create_user("mila@example.com", "Long-enough-pass-42")
        response = self.client.post(
            reverse("accounts:login"), {"username": "mila@example.com", "password": "Long-enough-pass-42"}
        )
        self.assertRedirects(response, reverse("accounts:dashboard"))

    def test_dashboard_requires_login(self):
        response = self.client.get(reverse("accounts:dashboard"))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse("accounts:login"), response["Location"])
