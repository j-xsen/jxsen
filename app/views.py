from django.shortcuts import render, redirect

from django.http import HttpResponse

from django.shortcuts import get_object_or_404
import app.models

# Create your views here.

def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


def epk(request):
    return render(request, "epk.html")


def lnk(request, short_url):
    obj = get_object_or_404(app.models.Lnk, short_url=short_url)
    if obj:
        obj.views += 1
        obj.save()
        return redirect(obj.long_url)
    else:
        return index(request)


def songlnk(request, song_name):
    obj = get_object_or_404(app.models.Song, url=song_name)
    links = app.models.SongLnk.objects.filter(song=obj.id)

    return render(request, "song.html",
                  {
                      'title': song_name,
                      'links': links,
                      'cover_art': obj.cover_art,
                      'desc': obj.desc,
                  })


def songs(request):
    song_list = app.models.Song.objects.all()
    return render(request, "songs.html",
                  {
                      'songs': song_list,
                  })
