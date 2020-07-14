from django.shortcuts import render

# Create your views here.
from django.db import modelsfrom django.contrib.auth.models import AbstractUser


def list_album[request]:
  mymusic = Album.objects.all(
  return render (request"mymusic/list_albums.html",{"mymusic": mymusic})