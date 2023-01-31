from django.shortcuts import render, redirect

from django.http import HttpResponse



# Create your views here.

def index(request):

    # return HttpResponse('Hello from Python!')

    return render(request, "index.html")



def epk(request):

    return render(request, "epk.html")



def lnk(request, name):

    if name == "bathe":

        return redirect("https://distrokid.com/hyperfollow/jaxsen/bathe")

    else:

        return index(request)


