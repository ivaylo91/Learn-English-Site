import re
import unicodedata

from django.conf import settings
from django.db import models
from django.urls import reverse

from apps.accounts.models import CEFRLevel
from apps.core.theme import LESSON_KINDS, LEVEL_COLORS, theme


def normalize_answer(text):
    """Lowercase, unify apostrophes, drop punctuation and extra spaces."""
    text = unicodedata.normalize("NFKC", text or "").lower()
    text = text.replace("’", "'").replace("‘", "'")
    text = re.sub(r"[.,!?;:\"]", "", text)
    return re.sub(r"\s+", " ", text).strip()


class Level(models.Model):
    code = models.CharField("код", max_length=2, choices=CEFRLevel.choices, unique=True)
    title = models.CharField("заглавие", max_length=80)
    summary = models.CharField("кратко описание", max_length=200)
    description = models.TextField("описание", blank=True)
    order = models.PositiveSmallIntegerField("ред", default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "ниво"
        verbose_name_plural = "нива"

    def __str__(self):
        return f"{self.code} {self.title}"

    def get_absolute_url(self):
        return reverse("courses:level", args=[self.code.lower()])

    @property
    def theme(self):
        return theme(LEVEL_COLORS.get(self.code))


class Unit(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name="units", verbose_name="ниво")
    title = models.CharField("заглавие", max_length=120)
    slug = models.SlugField(unique=True)
    summary = models.CharField("кратко описание", max_length=200, blank=True)
    icon = models.CharField("икона (Font Awesome)", max_length=40, default="fa-book-open")
    order = models.PositiveSmallIntegerField("ред", default=0)

    class Meta:
        ordering = ["level__order", "order"]
        verbose_name = "раздел"
        verbose_name_plural = "раздели"

    def __str__(self):
        return f"{self.level.code} {self.title}"


class Lesson(models.Model):
    class Kind(models.TextChoices):
        GRAMMAR = "grammar", "Граматика"
        VOCABULARY = "vocabulary", "Речник"
        CONVERSATION = "conversation", "Разговор"
        READING = "reading", "Четене"
        LISTENING = "listening", "Слушане"

    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name="lessons", verbose_name="раздел")
    title = models.CharField("заглавие", max_length=120)
    title_en = models.CharField("заглавие на английски", max_length=120, blank=True)
    slug = models.SlugField(unique=True)
    kind = models.CharField("вид", max_length=20, choices=Kind.choices, default=Kind.GRAMMAR)
    summary = models.CharField("кратко описание", max_length=200, blank=True)
    theory = models.TextField("теория (HTML)", blank=True, help_text="Обяснение на български. Позволен е HTML.")
    dialogue = models.TextField(
        "диалог", blank=True,
        help_text="За уроци по слушане. Всеки ред: Говорител | Английски текст | Превод на български",
    )
    audio = models.FileField(
        "аудио файл", upload_to="lessons/audio/", blank=True,
        help_text="По желание. Ако няма файл, диалогът се чете от гласа на браузъра.",
    )
    order = models.PositiveSmallIntegerField("ред", default=0)
    minutes = models.PositiveSmallIntegerField("минути", default=5)
    xp_reward = models.PositiveSmallIntegerField("XP награда", default=10)
    is_premium = models.BooleanField("премиум", default=False)
    is_published = models.BooleanField("публикуван", default=True)

    class Meta:
        ordering = ["unit__level__order", "unit__order", "order"]
        verbose_name = "урок"
        verbose_name_plural = "уроци"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("courses:lesson", args=[self.slug])

    @property
    def level(self):
        return self.unit.level

    def is_locked_for(self, user):
        return self.is_premium and not (user.is_authenticated and user.is_premium)

    @property
    def kind_theme(self):
        color, icon = LESSON_KINDS.get(self.kind, ("teal", "fa-book"))
        return {**theme(color), "icon": icon}

    def dialogue_lines(self):
        """Parse the dialogue field into [{speaker, who, en, bg}]; who is the speaker's index (0, 1, ...)."""
        lines, speakers = [], []
        for raw in self.dialogue.splitlines():
            parts = [p.strip() for p in raw.split("|")]
            if len(parts) >= 2 and parts[1]:
                if parts[0] not in speakers:
                    speakers.append(parts[0])
                lines.append({
                    "speaker": parts[0], "who": speakers.index(parts[0]),
                    "en": parts[1], "bg": parts[2] if len(parts) > 2 else "",
                })
        return lines


class Exercise(models.Model):
    class Type(models.TextChoices):
        CHOICE = "choice", "Избор на отговор"
        FILL = "fill", "Попълни празното"
        TRANSLATE = "translate", "Преведи"
        DICTATION = "dictation", "Диктовка"

    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="exercises", verbose_name="урок")
    type = models.CharField("тип", max_length=10, choices=Type.choices, default=Type.CHOICE)
    instruction = models.CharField("инструкция", max_length=200, blank=True)
    prompt = models.CharField("задача", max_length=300, help_text="За „Попълни“ използвайте ___ за празното място.")
    audio_text = models.CharField(
        "текст за слушане", max_length=300, blank=True,
        help_text="Ако е попълнено, ученикът чува този текст. При „Диктовка“ това е и верният отговор.",
    )
    answers = models.CharField(
        "верни отговори", max_length=300, blank=True,
        help_text="За „Попълни“ и „Преведи“. Няколко варианта се разделят с |",
    )
    explanation = models.CharField("обяснение", max_length=300, blank=True)
    order = models.PositiveSmallIntegerField("ред", default=0)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "упражнение"
        verbose_name_plural = "упражнения"

    def __str__(self):
        return self.prompt

    def accepted_answers(self):
        if self.type == self.Type.CHOICE:
            return [c.text for c in self.choices.all() if c.is_correct]
        answers = [a.strip() for a in self.answers.split("|") if a.strip()]
        if not answers and self.type == self.Type.DICTATION and self.audio_text:
            answers = [self.audio_text]
        return answers

    def is_correct_answer(self, value):
        """Return True when value is a correct answer. Choices are checked by id."""
        if self.type == self.Type.CHOICE:
            if not str(value).isdigit():
                return False
            return self.choices.filter(pk=int(value), is_correct=True).exists()
        given = normalize_answer(str(value))
        return any(given == normalize_answer(a) for a in self.accepted_answers())


class Choice(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name="choices")
    text = models.CharField("текст", max_length=200)
    is_correct = models.BooleanField("верен", default=False)

    class Meta:
        ordering = ["id"]
        verbose_name = "отговор"
        verbose_name_plural = "отговори"

    def __str__(self):
        return self.text


class LessonProgress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="lesson_progress")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="progress")
    best_score = models.PositiveSmallIntegerField("най-добър резултат (%)", default=0)
    attempts = models.PositiveIntegerField("опити", default=0)
    completed_at = models.DateTimeField("завършен", null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [("user", "lesson")]
        verbose_name = "прогрес по урок"
        verbose_name_plural = "прогрес по уроци"

    @property
    def is_completed(self):
        return self.completed_at is not None
