from datetime import timedelta

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils import timezone


class CEFRLevel(models.TextChoices):
    A1 = "A1", "A1 Начинаещи"
    A2 = "A2", "A2 Основно ниво"
    B1 = "B1", "B1 Средно ниво"
    B2 = "B2", "B2 Над средното"
    C1 = "C1", "C1 Напреднали"
    C2 = "C2", "C2 Владеене"


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Имейлът е задължителен.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    class Goal(models.TextChoices):
        TRAVEL = "travel", "Пътуване"
        WORK = "work", "Работа и кариера"
        STUDY = "study", "Учене и изпити"
        GENERAL = "general", "За себе си"

    class Plan(models.TextChoices):
        FREE = "free", "Безплатен"
        PREMIUM = "premium", "Премиум"

    username = None
    email = models.EmailField("имейл", unique=True)
    display_name = models.CharField("име", max_length=60, blank=True)
    level = models.CharField("ниво", max_length=2, choices=CEFRLevel.choices, blank=True)
    goal = models.CharField("цел", max_length=10, choices=Goal.choices, default=Goal.GENERAL)
    daily_goal_xp = models.PositiveSmallIntegerField("дневна цел (XP)", default=30)
    xp = models.PositiveIntegerField("точки опит", default=0)
    current_streak = models.PositiveIntegerField("поредни дни", default=0)
    longest_streak = models.PositiveIntegerField("най-дълга серия", default=0)
    last_activity_date = models.DateField("последна активност", null=True, blank=True)
    plan = models.CharField("план", max_length=10, choices=Plan.choices, default=Plan.FREE)
    premium_until = models.DateTimeField("премиум до", null=True, blank=True)
    show_in_leaderboard = models.BooleanField("показвай ме в класацията", default=True, db_default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = "потребител"
        verbose_name_plural = "потребители"

    def __str__(self):
        return self.display_name or self.email

    @property
    def name(self):
        return self.display_name or self.email.split("@")[0]

    @property
    def is_premium(self):
        if self.plan != self.Plan.PREMIUM:
            return False
        return self.premium_until is None or self.premium_until > timezone.now()

    def streak_is_active(self):
        if not self.last_activity_date:
            return False
        return self.last_activity_date >= timezone.localdate() - timedelta(days=1)

    def add_xp(self, amount):
        """Add XP, update the daily streak and save the user."""
        today = timezone.localdate()
        if self.last_activity_date != today:
            if self.last_activity_date == today - timedelta(days=1):
                self.current_streak += 1
            else:
                self.current_streak = 1
            self.last_activity_date = today
        self.longest_streak = max(self.longest_streak, self.current_streak)
        self.xp += amount
        self.save(update_fields=["xp", "current_streak", "longest_streak", "last_activity_date"])
        XPEvent.objects.create(user=self, amount=amount)

    def xp_today(self):
        today = timezone.localdate()
        return self.xp_events.filter(created_at__date=today).aggregate(total=models.Sum("amount"))["total"] or 0


class XPEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="xp_events")
    amount = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = "събитие XP"
        verbose_name_plural = "събития XP"
