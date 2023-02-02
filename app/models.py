from django.db import models


# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=32)
    release_date = models.DateField()
    cover_art = models.URLField()
    desc = models.CharField(default="FART BUTT POOP", max_length=360)

    def __str__(self):
        return self.title


class SongLnk(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    dest_url = models.URLField(max_length=200)
    icon = models.CharField(max_length=32)

    def __str__(self):
        return self.song.title + " - " + self.name


class Lnk(models.Model):
    long_url = models.URLField(max_length=200)
    short_url = models.CharField(max_length=30)
    views = models.IntegerField(default=0)
