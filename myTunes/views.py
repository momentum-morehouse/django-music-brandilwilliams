from django.shortcuts import render
from .models import Album

def index(request):
  albums = Album.objects.all()
  return render (request, "myTunes/list_albums.html", context={"albums": albums})