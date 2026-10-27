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


class AchievementLeaderboardTests(TestCase):
    def test_achievements_follow_stats(self):
        from .achievements import achievements_for

        user = User.objects.create_user("x@example.com", "pass")
        earned = {a["key"] for a in achievements_for(user) if a["earned"]}
        self.assertEqual(earned, set())
        user.add_xp(150)
        earned = {a["key"] for a in achievements_for(user) if a["earned"]}
        self.assertEqual(earned, {"xp-100"})

    def test_leaderboard_counts_this_week_and_respects_opt_out(self):
        a = User.objects.create_user("a@example.com", "pass", display_name="Ана")
        b = User.objects.create_user("b@example.com", "pass", display_name="Боби", show_in_leaderboard=False)
        c = User.objects.create_user("c@example.com", "pass", display_name="Цвети")
        a.add_xp(10)
        b.add_xp(50)
        c.add_xp(20)
        # Points from last month don't count.
        a.xp_events.update(created_at=timezone.now() - timedelta(days=40))
        response = self.client.get(reverse("core:leaderboard"))
        self.assertEqual([u.display_name for u in response.context["leaders"]], ["Цвети"])
        self.assertNotContains(response, "Боби")


class DeleteAccountTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("del@example.com", "pass")
        self.client.force_login(self.user)

    def test_wrong_email_keeps_account(self):
        self.client.post(reverse("accounts:delete"), {"confirm_email": "other@example.com"})
        self.assertTrue(User.objects.filter(pk=self.user.pk).exists())

    def test_matching_email_deletes_account_and_logs_out(self):
        self.user.add_xp(10)
        response = self.client.post(reverse("accounts:delete"), {"confirm_email": "DEL@example.com "})
        self.assertRedirects(response, reverse("core:home"))
        self.assertFalse(User.objects.filter(pk=self.user.pk).exists())
        self.assertNotIn("_auth_user_id", self.client.session)
