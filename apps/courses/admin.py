from django.contrib import admin

from .models import Choice, Exercise, Lesson, LessonProgress, Level, Unit


class UnitInline(admin.TabularInline):
    model = Unit
    extra = 0
    prepopulated_fields = {"slug": ["title"]}


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ["code", "title", "order"]
    inlines = [UnitInline]


class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 0
    fields = ["title", "slug", "kind", "order", "is_premium", "is_published"]
    prepopulated_fields = {"slug": ["title"]}


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ["title", "level", "order"]
    list_filter = ["level"]
    prepopulated_fields = {"slug": ["title"]}
    inlines = [LessonInline]


class ExerciseInline(admin.StackedInline):
    model = Exercise
    extra = 0
    show_change_link = True


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ["title", "unit", "kind", "order", "xp_reward", "is_premium", "is_published"]
    list_filter = ["unit__level", "kind", "is_premium", "is_published"]
    list_editable = ["order", "is_premium", "is_published"]
    search_fields = ["title", "title_en"]
    prepopulated_fields = {"slug": ["title_en"]}
    inlines = [ExerciseInline]


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ["prompt", "lesson", "type", "order"]
    list_filter = ["type", "lesson__unit__level"]
    search_fields = ["prompt"]
    inlines = [ChoiceInline]


@admin.register(LessonProgress)
class LessonProgressAdmin(admin.ModelAdmin):
    list_display = ["user", "lesson", "best_score", "attempts", "completed_at"]
    list_select_related = ["user", "lesson"]
