from django.shortcuts import render, redirect
import requests, json
from django.http import HttpResponse

from django.shortcuts import get_object_or_404
import app.models as models

# Create your views here.

def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


def epk(request):
    return render(request, "epk.html")


api_key = '---'
api_url = 'https://ipgeolocation.abstractapi.com/v1/?api_key=' + api_key


def get_ip_geolocation_data(ip_address):
    response = requests.get(api_url + "&ip_address=" + ip_address)
    #response = requests.get(api_url)
    return response.content


def lnk(request, short_url):
    obj = get_object_or_404(models.Lnk, short_url=short_url)
    if obj:
        obj.views += 1
        obj.save()

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        geoloc_json = get_ip_geolocation_data(ip)
        geoloc_data = json.loads(geoloc_json)

        if geoloc_data['city']:
            print(geoloc_data)
            country = geoloc_data['country']
            region = geoloc_data['region']
            city = geoloc_data['city']

            loc_obj, loc_created = models.Location.objects.get_or_create(
                country=country,
                region=region,
                city=city
            )

            log = models.LnkLog.objects.create(lnk=obj, ip=ip, location=loc_obj)

        return redirect(obj.long_url)
    else:
        return index(request)


def songlnk(request, song_name):
    obj = get_object_or_404(models.Song, title=song_name)
    links = models.SongLnk.objects.filter(song=obj.id)

    return redirect(obj.redirect_url)


def songs(request):
    song_list = models.Song.objects.all()
    return render(request, "songs.html",
                  {
                      'songs': song_list,
                  })
