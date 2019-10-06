from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request, "home.html",)


def count(request):
    fulltext = request.GET['fulltext']
    # Split the text into strings wherever there is a space
    wordlist = fulltext.split()
    # Count the number of words
    count = len(wordlist)

    # Create empty dict and if the word appears,
    # add it to the dict and set count as 1.
    # If the word is already in the dict,
    # increment existing count
    wordDict = {}
    for word in wordlist:
        if word in wordDict:
            wordDict[word] += 1
        else:
            wordDict[word] = 1

    # Sort the words based on the key (counttotal)
    # Reverse the order, so we go from high to low
    sortedWords = sorted(wordDict.items(),
                         key=operator.itemgetter(1),
                         reverse=True)

    context = {
        "fulltext": fulltext,
        "count": count,
        # Change the wordDict to a list to enable HTML injection
        "sortedWords": sortedWords,
        }
    return render(request, "count.html", context)
