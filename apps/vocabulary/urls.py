from django.urls import path

from . import views

app_name = "vocabulary"

urlpatterns = [
    path("", views.topic_list, name="topics"),
    path("travel/", views.travel, name="travel"),
    path("<slug:slug>/", views.topic_detail, name="topic"),
]
