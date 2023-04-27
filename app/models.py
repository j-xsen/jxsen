from django.db import models


# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=32)
    # url = models.CharField(max_length=32, default="ERROR")
    release_date = models.DateField()
    # cover_art = models.URLField()
    # desc = models.CharField(default="FART BUTT POOP", max_length=360)
    redirect_url = models.URLField(max_length=200, default="https://jxsen.com/")

    def __str__(self):
        return self.title


class Location(models.Model):
    country = models.CharField(max_length=32, blank=True)
    region = models.CharField(max_length=32, blank=True)
    city = models.CharField(max_length=32, blank=True)

    def __str__(self):
        return self.city + ", " + self.region + ", " + self.country


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

    def __str__(self):
        return self.short_url + ' (' + str(self.views) + ')'


class LnkLog(models.Model):
    lnk = models.ForeignKey(Lnk, on_delete=models.CASCADE)
    ip = models.CharField(max_length=32)
    location = models.ForeignKey(Location, blank=True, null=True, on_delete=models.SET_NULL)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.lnk) + ' - ' + str(self.ip)
