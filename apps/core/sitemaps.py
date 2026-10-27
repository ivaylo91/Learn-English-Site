from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from apps.courses.models import Lesson, Level
from apps.vocabulary.models import Topic


class StaticSitemap(Sitemap):
    priority = 0.8
    changefreq = "weekly"

    def items(self):
        return ["core:home", "courses:levels", "courses:listening", "vocabulary:topics", "vocabulary:travel",
                "placement:test", "core:about", "core:faq", "core:privacy", "core:terms"]

    def location(self, item):
        return reverse(item)


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
