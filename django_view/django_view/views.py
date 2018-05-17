from django.http import HttpResponse
from django.http import JsonResponse
from datetime import datetime
import os



def time_now(request):
    now = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")

    return HttpResponse("Now is: {0}".format(now))

def lst_folders(request):
    """ каталог из которого будем брать файлы"""


    # получаем список файлов в переменную files
    files = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return HttpResponse(files)
def addres(request):
    dct = {
    "host":"localhost",
    "port":8080,
    "service":"dummy"
    }
    return JsonResponse(dct)
