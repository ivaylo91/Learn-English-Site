from django.urls import path

from apps.accounts.views import leaderboard

from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("leaderboard/", leaderboard, name="leaderboard"),
    path("about/", views.about, name="about"),
    path("faq/", views.faq, name="faq"),
    path("privacy/", views.page, {"template": "core/privacy.html"}, name="privacy"),
    path("terms/", views.page, {"template": "core/terms.html"}, name="terms"),
]
