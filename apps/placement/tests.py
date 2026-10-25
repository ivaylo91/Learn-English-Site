from django.test import SimpleTestCase

from .views import recommend_level


class RecommendLevelTests(SimpleTestCase):
    def test_starts_at_first_failed_level(self):
        self.assertEqual(recommend_level({"A1": (3, 3), "A2": (2, 3), "B1": (1, 3)}), "B1")

    def test_zero_correct_is_a1(self):
        self.assertEqual(recommend_level({"A1": (0, 3), "A2": (0, 3)}), "A1")

    def test_all_passed_is_top_level(self):
        self.assertEqual(recommend_level({c: (3, 3) for c in ["A1", "A2", "B1", "B2", "C1", "C2"]}), "C2")
