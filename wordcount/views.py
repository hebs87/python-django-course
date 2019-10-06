from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello World!")


def dogs(request):
    return HttpResponse("<h1>Dogs are great!</h1>")
