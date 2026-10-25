from django.urls import path

from . import views

app_name = "vocabulary"

urlpatterns = [
    path("", views.topic_list, name="topics"),
    path("travel/", views.travel, name="travel"),
    path("my-words/", views.my_words, name="my_words"),
    path("review/", views.review, name="review"),
    path("review/<int:saved_id>/", views.review_answer, name="review_answer"),
    path("save/<int:word_id>/", views.toggle_saved, name="toggle_saved"),
    # Topic slugs last: they would otherwise swallow the fixed paths above.
    path("<slug:slug>/save-all/", views.save_topic, name="save_topic"),
    path("<slug:slug>/", views.topic_detail, name="topic"),
]
