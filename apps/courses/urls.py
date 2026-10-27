from django.urls import path

from . import views

app_name = "courses"

urlpatterns = [
    path("", views.level_list, name="levels"),
    path("listening/", views.listening, name="listening"),
    path("category/<slug:key>/", views.category_detail, name="category"),
    path("check/", views.check_any, name="check_any"),
    path("mistakes/", views.mistakes, name="mistakes"),
    path("mistakes/complete/", views.complete_mistakes, name="mistakes_complete"),
    path("level/<str:code>/", views.level_detail, name="level"),
    path("lesson/<slug:slug>/", views.lesson_detail, name="lesson"),
    path("lesson/<slug:slug>/check/", views.check_exercise, name="check"),
    path("lesson/<slug:slug>/complete/", views.complete_lesson, name="complete"),
]
