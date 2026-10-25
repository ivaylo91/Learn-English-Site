from django.urls import path

from . import views

app_name = "placement"

urlpatterns = [
    path("", views.test, name="test"),
    path("result/", views.result, name="result"),
]
