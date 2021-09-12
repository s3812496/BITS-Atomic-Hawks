from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('song/<int:Song_id>', views.song_by_id, name='song_by_id'),
    path('artist/<int:Artist_id>', views.artist_by_id, name='artist_by_id'),
    path('album/<int:Song_id>', views.album_by_id, name='album_by_id'),
]