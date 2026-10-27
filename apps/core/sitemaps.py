from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from apps.courses.categories import CATEGORIES
from apps.courses.models import Lesson, Level
from apps.vocabulary.models import Topic


class StaticSitemap(Sitemap):
    priority = 0.8
    changefreq = "weekly"

    def items(self):
        categories = [("courses:category", key) for key in CATEGORIES]
        pages = ["core:home", "courses:levels", "vocabulary:topics", "vocabulary:travel",
                 "placement:test", "core:about", "core:faq", "core:privacy", "core:terms"]
        return [(name, None) for name in pages] + categories

    def location(self, item):
        name, key = item
        return reverse(name, args=[key]) if key else reverse(name)


class LevelSitemap(Sitemap):
    priority = 0.7
    changefreq = "weekly"

    def items(self):
        return Level.objects.all()


class LessonSitemap(Sitemap):
    priority = 0.6
    changefreq = "monthly"

    def items(self):
        return Lesson.objects.filter(is_published=True, is_premium=False)


class TopicSitemap(Sitemap):
    priority = 0.6
    changefreq = "monthly"

    def items(self):
        return Topic.objects.filter(is_premium=False)


SITEMAPS = {"static": StaticSitemap, "levels": LevelSitemap, "lessons": LessonSitemap, "topics": TopicSitemap}
