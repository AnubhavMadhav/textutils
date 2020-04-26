# I have created this file - Anubhav Madhav

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # params = {'name':'Anubhav', 'place':'India'}            # We can use dictionary to use variables in templates.
    return render(request, 'index.html')            # passed the dictionary as 3rd argument
    # home = '''<h1> Home <h1>
    # <a href="http://127.0.0.1:8000/removepunc">Remove Punctuations</a><br>
    # <a href="http://127.0.0.1:8000/capitalizefirst">Capitalize First</a><br>
    # <a href="http://127.0.0.1:8000/newlineremove">Remove New Line</a><br>
    # <a href="http://127.0.0.1:8000/spaceremove">Remove Space</a><br>
    # <a href="http://127.0.0.1:8000/charcount">Count Characters</a><br>
    # '''
    # return HttpResponse(home)

def navigate(request):
    nav = '''<h1>Navigate</h1>
    <a href="https://www.linkedin.com/">LinkedIn</a><br>
    <a href="https://twitter.com/">Twitter</a><br>
    <a href="https://github.com/">GitHub</a><br>
    <a href="https://www.facebook.com/">Facebook</a>
    '''
    return HttpResponse(nav)


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
    # print(removepunc)
    # print(djtext)
    # a = '''<h1>Remove Punctuations</h1>
    # <a href="http://127.0.0.1:8000/" ><button>Home</button></a>
    # '''
    # analyzed = djtext               # for now

    # Check which checkbox is on
    if removepunc == "on":
        analyzed = ""
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^`{|}~'''       # removed 'space' from this list       # Punctuation List of Python found on Internet
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        djtext = analyzed
        params = {'purpose':'Removed Punctuations','analyzed_text':analyzed}
        # Analyze the Text
        # return render(request, 'analyze.html', params)
    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        djtext = analyzed
        params = {'purpose': 'Capitalized Text', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':           # we need to check for both '\n' and '\r' for newline
                analyzed = analyzed + char
        params = {'purpose': 'Removed New Line', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if spaceremover == "on":
        analyzed = ""
        for char in djtext:
            if char != ' ':
                analyzed = analyzed + char
        params = {'purpose': 'Removed Space', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if charcount == "on":
        analyzed = ""
        c = 0
        for char in djtext:
            c += 1
        params = {'purpose': 'Count total no. of characters', 'analyzed_text': 'Total no.of characters = ' + str(c)}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index + 1] == " ":
                pass
            else:
                analyzed = analyzed + char

        params = {'purpose': 'Extra Spaces Removed', 'analyzed_text': analyzed}
        # djtext = analyzed
        # return render(request, 'analyze.html', params)

    if removepunc != "on" and fullcaps != "on" and newlineremover != "on" and spaceremover != "on" and charcount != "on" and extraspaceremover != "on":
        return HttpResponse("Error!! Select something and then try again.")


    return render(request, 'analyze.html', params)

# def capitalizefirst(request):
#     b = '''<h1>Capitalize First</h1>
#     <a href="http://127.0.0.1:8000/" ><button>Home</button></a>
#     '''
#     return HttpResponse(b)
#
#
# def newlineremove(request):
#     c = '''<h1>Remove New Line</h1>
#     <a href="http://127.0.0.1:8000/" ><button>Home</button></a>
#     '''
#     return HttpResponse(c)
#
#
# def spaceremove(request):
#     d = '''<h1>Remove Space</h1>
#     <a href="http://127.0.0.1:8000/" ><button>Home</button></a>
#     '''
#     return HttpResponse(d)
#
#
# def charcount(request):
#     e = '''<h1>Count Characters</h1>
#     <a href="http://127.0.0.1:8000/" ><button>Home</button></a>
#     '''
#     return HttpResponse(e)
#
