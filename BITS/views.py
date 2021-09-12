from django.shortcuts import render
from django.http import HttpResponse
from .models import Song, Artist, Album

# Create your views here.

def index(request):
    return render(request, 'index.html')

def song_by_id(request, Song_id):
    Song = Song.objects.get(pk=Song_id)
    return render(request, 'index.html')