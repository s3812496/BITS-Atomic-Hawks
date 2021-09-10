from django.db import models

# Create your models here.

class Artist(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(null = True, blank = True, upload_to="images/")

class Album(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    image = models.ImageField(null = True, blank = True, upload_to="images/")

class Song(models.Model):
    title = models.CharField(max_length=200)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    description = models.TextField()
    release_date = models.DateField()
    length_min = models.FloatField()
    producer = models.CharField(max_length=1000)