from django.db import models

# Create your models here.

class Artist(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(null = True, blank = True, upload_to="images/")

    def __str__(self):
        return self.title

class Album(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    image = models.ImageField(null = True, blank = True, upload_to="images/")
    Spotify_Embeded_Code = models.CharField(max_length=300)

    def __str__(self):
        return self.title

class Song(models.Model):
    title = models.CharField(max_length=200)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    lryics = models.TextField()
    release_date = models.DateField()
    length_min = models.FloatField()
    producer = models.CharField(max_length=1000)
    Spotify_Embeded_Code = models.CharField(max_length=300)

    def __str__(self):
        return self.title