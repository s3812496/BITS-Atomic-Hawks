from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('song/<int:Song.id>', views.song_by_id, name='song_by_id'),
]