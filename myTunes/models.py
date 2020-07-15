from django.db import models

# Create your models here.

class Album(models.Model):
    artist_name = models.CharField(max_length=255, null=True, blank=True)
    album_title = models.CharField(max_length=255, null=True, blank=True)
    release_date = models.DateField(max_length=255, null=True, blank=True)
    image_url = models.TextField(null=True, blank=True)


    # def __str__(self):
    #   return f"{self.albumtitle} by {self.artistname}"

# class Users(models.Model):
#   pass