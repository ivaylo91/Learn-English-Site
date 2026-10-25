from django.db import models
from django.urls import reverse

from apps.accounts.models import CEFRLevel
from apps.core.theme import COLOR_CHOICES, theme


class Topic(models.Model):
    title = models.CharField("заглавие", max_length=100)
    title_en = models.CharField("заглавие на английски", max_length=100, blank=True)
    slug = models.SlugField(unique=True)
    summary = models.CharField("кратко описание", max_length=200, blank=True)
    icon = models.CharField("икона (Font Awesome)", max_length=40, default="fa-comments")
    color = models.CharField("цвят", max_length=10, choices=COLOR_CHOICES, default="teal")
    level = models.CharField("ниво", max_length=2, choices=CEFRLevel.choices, default=CEFRLevel.A1)
    is_travel = models.BooleanField("за пътуване", default=False)
    is_premium = models.BooleanField("премиум", default=False)
    order = models.PositiveSmallIntegerField("ред", default=0)

    class Meta:
        ordering = ["order", "title"]
        verbose_name = "тема"
        verbose_name_plural = "теми"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("vocabulary:topic", args=[self.slug])

    @property
    def theme(self):
        return theme(self.color)


class Word(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="words", verbose_name="тема")
    english = models.CharField("на английски", max_length=200)
    bulgarian = models.CharField("на български", max_length=200)
    transcription = models.CharField("произношение", max_length=120, blank=True)
    example_en = models.CharField("пример (EN)", max_length=300, blank=True)
    example_bg = models.CharField("пример (BG)", max_length=300, blank=True)
    order = models.PositiveSmallIntegerField("ред", default=0)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "дума или фраза"
        verbose_name_plural = "думи и фрази"

    def __str__(self):
        return self.english
