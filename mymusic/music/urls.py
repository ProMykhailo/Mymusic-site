from django.urls import path
from . import views

urlpatterns = [
    # Головна сторінка нашого музичного додатка
    path('', views.music_list, name='music_list'),
]