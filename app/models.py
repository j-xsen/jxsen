from django.db import models


# Create your models here.
class Lnk(models.Model):
    long_url = models.URLField(max_length=200)
    short_url = models.CharField(max_length=30)
    views = models.IntegerField(default=0)
