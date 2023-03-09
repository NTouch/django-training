from django.shortcuts import render

# Create your views here.
from .controllers.controller import AppController

controller = AppController()


def index(request):
    if request.POST.get('user_query') is not None:
        gifs = controller.query_gifs(request.POST.get('user_query'))
        print(gifs[0].size['width'])
        print(gifs[2].size['height'])
        return render(request, "index.html", {'gifs': gifs})

    return render(request, "index.html")
