from django.contrib import admin
from .models import Lnk, Song, SongLnk, Location, LnkLog

# Register your models here.
admin.site.register(Song)
admin.site.register(SongLnk)
admin.site.register(Lnk)
admin.site.register(Location)
admin.site.register(LnkLog)
