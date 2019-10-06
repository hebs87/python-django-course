from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def dogs(request):
    return HttpResponse("<h1>Dogs are great!</h1>")
