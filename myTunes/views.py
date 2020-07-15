from django.shortcuts import render
from .models import Album, Users

def index(request):
  mymusic = Album.objects.all()
  return render (request, "myTunes/list_albums.html", context={"myTunes": mymusic})