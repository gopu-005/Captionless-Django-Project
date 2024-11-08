from django.urls import path
from . import views

urlpatterns = [
    path('', views.video_summarizer, name='video_summarizer'),
]