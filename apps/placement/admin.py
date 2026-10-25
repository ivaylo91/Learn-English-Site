from django.contrib import admin

from .models import PlacementChoice, PlacementQuestion


class PlacementChoiceInline(admin.TabularInline):
    model = PlacementChoice
    extra = 3


@admin.register(PlacementQuestion)
class PlacementQuestionAdmin(admin.ModelAdmin):
    list_display = ["prompt", "level", "order"]
    list_filter = ["level"]
    inlines = [PlacementChoiceInline]
