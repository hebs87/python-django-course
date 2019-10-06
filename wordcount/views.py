from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    context = {"description": "This is a word count site"}
    return render(request, "home.html", context)


def dogs(request):
    return HttpResponse("<h1>Dogs are great!</h1>")
