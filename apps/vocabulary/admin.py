from django.contrib import admin

from .models import Topic, Word


class WordInline(admin.TabularInline):
    model = Word
    extra = 1


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ["title", "level", "is_travel", "is_premium", "order"]
    list_filter = ["level", "is_travel", "is_premium"]
    prepopulated_fields = {"slug": ["title_en"]}
    inlines = [WordInline]
