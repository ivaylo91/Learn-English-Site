from datetime import timedelta

from django.db import models
from django.urls import reverse
from django.utils import timezone

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


class SavedWord(models.Model):
    """A word in the learner's review deck, scheduled with Leitner boxes."""

    # Days until the next review for each box. A correct answer moves the word up one box.
    INTERVALS = {1: 1, 2: 3, 3: 7, 4: 14, 5: 30}
    MAX_BOX = 5

    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name="saved_words")
    word = models.ForeignKey(Word, on_delete=models.CASCADE, related_name="saved_by")
    box = models.PositiveSmallIntegerField("кутия", default=1)
    due_date = models.DateField("следващ преговор", default=timezone.localdate)
    reviews = models.PositiveIntegerField("прегледи", default=0)
    correct = models.PositiveIntegerField("верни", default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [("user", "word")]
        ordering = ["due_date", "box"]
        verbose_name = "запазена дума"
        verbose_name_plural = "запазени думи"

    def __str__(self):
        return f"{self.user} - {self.word}"

    @property
    def is_due(self):
        return self.due_date <= timezone.localdate()

    @property
    def is_mastered(self):
        return self.box >= self.MAX_BOX

    def record(self, knew_it):
        """Apply a review result and reschedule. Returns True if this review counted (the word was due)."""
        was_due = self.is_due
        self.reviews += 1
        if knew_it:
            self.correct += 1
            if was_due:
                self.box = min(self.box + 1, self.MAX_BOX)
                self.due_date = timezone.localdate() + timedelta(days=self.INTERVALS[self.box])
        else:
            self.box = 1
            self.due_date = timezone.localdate()
        self.save()
        return was_due
