from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import User


class StyledFormMixin:
    """Add Tailwind classes to text inputs and selects."""

    def style_fields(self):
        for name, field in self.fields.items():
            widget = field.widget
            if isinstance(widget, (forms.RadioSelect, forms.CheckboxInput, forms.CheckboxSelectMultiple)):
                continue
            widget.attrs["class"] = (widget.attrs.get("class", "") + " field-input").strip()
            if field.help_text:
                widget.attrs.setdefault("aria-describedby", f"id_{self.add_prefix(name)}_help")


class SignupForm(StyledFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ["display_name", "email"]
        labels = {"display_name": "Как да те наричаме?", "email": "Имейл"}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["display_name"].required = True
        self.fields["password1"].label = "Парола"
        self.fields["password2"].label = "Повтори паролата"
        self.fields["password1"].help_text = "Поне 8 символа, не само цифри."
        self.fields["password2"].help_text = ""
        self.fields["email"].widget.attrs["autocomplete"] = "email"
        self.fields["display_name"].widget.attrs["autocomplete"] = "given-name"
        self.style_fields()


class LoginForm(StyledFormMixin, AuthenticationForm):
    error_messages = {
        "invalid_login": "Грешен имейл или парола.",
        "inactive": "Този профил е деактивиран.",
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Имейл"
        self.fields["username"].widget.attrs["autocomplete"] = "email"
        self.fields["password"].label = "Парола"
        self.style_fields()


class ProfileForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = ["display_name", "goal", "level", "daily_goal_xp", "show_in_leaderboard"]
        labels = {
            "display_name": "Име",
            "goal": "Защо учиш английски?",
            "level": "Твоето ниво",
            "daily_goal_xp": "Дневна цел",
            "show_in_leaderboard": "Показвай името ми в седмичната класация",
        }
        widgets = {
            "goal": forms.RadioSelect,
            "daily_goal_xp": forms.Select(
                choices=[(10, "Лека: 10 XP"), (30, "Нормална: 30 XP"), (50, "Сериозна: 50 XP"), (100, "Интензивна: 100 XP")]
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["level"].choices = [("", "Не знам, ще направя теста")] + list(self.fields["level"].choices)[1:]
        self.style_fields()
