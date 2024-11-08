from django.urls import path
from . import views

urlpattrens = [
    path('', views.video_summarizer, name='video_summarizer'),
]