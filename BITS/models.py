from django.db import models

# Create your models here.

class Song(models.Model):
    title = models.CharField(max_length=200)

class Album(models.Model):
    title = models.CharField(max_length=200)

class Artist(models.Model):
    title = models.CharField(max_length=200)