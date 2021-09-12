from django.http.request import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse
from .models import Song, Artist, Album

# Create your views here.

def index(request):
    return render(request, 'index.html')

def song_by_id(request, Song_id):
    song = Song.objects.get(pk=Song_id)
    context=context = {'Song':song}
    return render(request, 'song_by_id.html', context=context)

def artist_by_id(request, Artist_id):
    ABLst = Album.objects.all() # Imports all albums in to a array for later
    artist = Artist.objects.get(pk=Artist_id)
    context=context = {'Artist':artist, 'Album' :ABLst}
    return render(request, 'artist_by_id.html', context=context)

def album_by_id(request, Album_id):
    SNGst = Song.objects.all() # Imports all Songs in to a array for later
    album = Album.objects.get(pk=Album_id)
    context=context = {'Album':album, 'Artist' :SNGst}
    return render(request, 'album_by_id.html', context=context)