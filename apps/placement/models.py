from django.db import models

from apps.accounts.models import CEFRLevel


class PlacementQuestion(models.Model):
    level = models.CharField("ниво", max_length=2, choices=CEFRLevel.choices)
    prompt = models.CharField("въпрос", max_length=300)
    order = models.PositiveSmallIntegerField("ред", default=0)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "въпрос за ниво"
        verbose_name_plural = "въпроси за ниво"

    def __str__(self):
        return f"{self.level}: {self.prompt}"


class PlacementChoice(models.Model):
    question = models.ForeignKey(PlacementQuestion, on_delete=models.CASCADE, related_name="choices")
    text = models.CharField("текст", max_length=200)
    is_correct = models.BooleanField("верен", default=False)

    class Meta:
        ordering = ["id"]
        verbose_name = "отговор"
        verbose_name_plural = "отговори"

    def __str__(self):
        return self.text
