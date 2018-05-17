from django.http import HttpResponse
from django.http import JsonResponse
from datetime import datetime
import os



def time_now(request):
    now = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
    return HttpResponse(""% now)
def lst_folders(request):
    direct = [ i for i in os.listdir(".") if os.path.isdir(i)]
    return HttpResponse(direct)
def addres(request):
    dct = {
    "host":"localhost",
    "port":8080,
    "service":"dummy"
    }
    return JsonResponse(dct)
