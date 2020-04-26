# I have created this file - Anubhav Madhav

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # params = {'name':'Anubhav', 'place':'India'}            # We can use dictionary to use variables in templates.
    return render(request, 'index.html')            # passed the dictionary as 3rd argument

def analyze(request):
    # Get the Text
    djtext = request.POST.get('text','default')                # Statement to get the values of the textarea and if not found then take default value
    # Check checkbox value
    removepunc = request.POST.get('removepunc','off')            # Here, default will be 'off'
    fullcaps = request.POST.get('fullcaps','off')            # Here, default will be 'off'
    newlineremover = request.POST.get('newlineremover','off')            # Here, default will be 'off'
    spaceremover = request.POST.get('spaceremover','off')            # Here, default will be 'off'
    extraspaceremover = request.POST.get('extraspaceremover','off')            # Here, default will be 'off'
    charcount = request.POST.get('charcount','off')            # Here, default will be 'off'

    # Check which checkbox is on
    if removepunc == "on":
        analyzed = ""
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^`{|}~'''       # removed 'space' from this list       # Punctuation List of Python found on Internet
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        djtext = analyzed
        params = {'purpose':'Removed Punctuations','analyzed_text':analyzed}

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        djtext = analyzed
        params = {'purpose': 'Capitalized Text', 'analyzed_text': analyzed}

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':           # we need to check for both '\n' and '\r' for newline
                analyzed = analyzed + char
        params = {'purpose': 'Removed New Line', 'analyzed_text': analyzed}
        djtext = analyzed

    if spaceremover == "on":
        analyzed = ""
        for char in djtext:
            if char != ' ':
                analyzed = analyzed + char
        params = {'purpose': 'Removed Space', 'analyzed_text': analyzed}
        djtext = analyzed

    if charcount == "on":
        analyzed = ""
        c = 0
        for char in djtext:
            c += 1
        params = {'purpose': 'Count total no. of characters', 'analyzed_text': 'Total no.of characters = ' + str(c)}
        djtext = analyzed

    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index + 1] == " ":
                pass
            else:
                analyzed = analyzed + char

        params = {'purpose': 'Extra Spaces Removed', 'analyzed_text': analyzed}

    if removepunc != "on" and fullcaps != "on" and newlineremover != "on" and spaceremover != "on" and charcount != "on" and extraspaceremover != "on":
        return HttpResponse("Error!! Select something and then try again.")


    return render(request, 'analyze.html', params)
