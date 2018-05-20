from django.http import HttpResponse
from django.http import JsonResponse
from datetime import datetime
import os

from django_view.models import Artist,Song


def time_now(request):
    now = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
    return HttpResponse("Now is: {}".format(now))


def lst_folders(request):
    """ каталог из которого будем брать файлы"""

    # получаем список файлов в переменную files
    files = os.path.dirname(__file__)
    return HttpResponse(files)


def addres(request):
    dct = {
    "host":"localhost",
    "port":8080,
    "service":"dummy"
    }
    return JsonResponse(dct)


def show_artists(request):
    artists = list(Artist.objects.all())
    response = [a.to_dict() for a in artists]
    return HttpResponse(response)


def add_artist(request):
    data = {
        'name': request.GET.get('name'),
        'surname': request.GET.get('surname'),
        'birth': request.GET.get('birth')
    }

    a = Artist.from_dict(data)
    a.save()
    return HttpResponse([a.to_dict()])
##########################################################################
def show_songs(request):
    songs = list(Song.objects.all())
    response = [b.to_dict() for b in songs]
    return HttpResponse(response)

def add_song(request):
    autor = Artist.objects.get(pk=int(request.GET.get('author')))
    data = {
        'name':request.GET.get('name'),
        'date_released':request.GET.get('date_released'),
        'author':autor
        }
    print(data)
    b = Song.from_dict(data)
    b.save()
    return HttpResponse([b.to_dict()])
