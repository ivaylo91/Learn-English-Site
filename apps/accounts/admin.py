from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User, XPEvent


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    ordering = ["-date_joined"]
    list_display = ["email", "display_name", "level", "goal", "xp", "current_streak", "plan", "is_staff"]
    list_filter = ["plan", "level", "goal", "is_staff", "is_active"]
    search_fields = ["email", "display_name"]
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Профил", {"fields": ["display_name", "level", "goal", "daily_goal_xp"]}),
        ("Прогрес", {"fields": ["xp", "current_streak", "longest_streak", "last_activity_date"]}),
        ("План", {"fields": ["plan", "premium_until"]}),
        ("Права", {"fields": ["is_active", "is_staff", "is_superuser", "groups", "user_permissions"]}),
        ("Дати", {"fields": ["last_login", "date_joined"]}),
    ]
    add_fieldsets = [(None, {"classes": ["wide"], "fields": ["email", "password1", "password2"]})]


@admin.register(XPEvent)
class XPEventAdmin(admin.ModelAdmin):
    list_display = ["user", "amount", "created_at"]
    list_select_related = ["user"]
