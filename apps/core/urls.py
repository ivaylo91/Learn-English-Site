from django.urls import path

from apps.accounts.views import leaderboard

from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("leaderboard/", leaderboard, name="leaderboard"),
]
