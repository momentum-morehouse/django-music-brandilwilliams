from django.db import models

# Create your models here.

class Album(model.Model):
    artistname = models.Charfield(max_length=255)
    albumtitle = models.Charfield
