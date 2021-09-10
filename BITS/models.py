from django.db import models

# Create your models here.

class Artist(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="images_artist")
    description = models.CharField(max_length=20000)

class Album(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='images_album')
    description = models.CharField(max_length=20000)
    release_date = models.DateField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

class Song(models.Model):
    title = models.CharField(max_length=200)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    description = models.CharField(max_length=20000)
    release_date = models.DateField()
    length_min = models.FloatField()
    producer = models.CharField(max_length=1000)



