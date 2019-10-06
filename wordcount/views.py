from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "home.html",)


def count(request):
    fulltext = request.GET['fulltext']
    # Split the text into strings wherever there is a space
    wordlist = fulltext.split()
    # Count the number of words
    count = len(wordlist)

    context = {"fulltext": fulltext, "count": count}
    return render(request, "count.html", context)
