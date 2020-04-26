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
    djtext = request.GET.get('text','default')                # Statement to get the values of the textarea and if not found then take default value
    # Check checkbox value
    removepunc = request.GET.get('removepunc','off')            # Here, default will be 'off'
    fullcaps = request.GET.get('fullcaps','off')            # Here, default will be 'off'
    newlineremover = request.GET.get('newlineremover','off')            # Here, default will be 'off'
    spaceremover = request.GET.get('spaceremover','off')            # Here, default will be 'off'
    extraspaceremover = request.GET.get('extraspaceremover','off')            # Here, default will be 'off'
    charcount = request.GET.get('charcount','off')            # Here, default will be 'off'
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
        params = {'purpose':'Removed Punctuations','analyzed_text':analyzed}
        # Analyze the Text
        return render(request, 'analyze.html', params)
    elif fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Capitalized Text', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char!= '\n':
                analyzed = analyzed + char
        params = {'purpose': 'Removed New Line', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif spaceremover == "on":
        analyzed = ""
        for char in djtext:
            if char != ' ':
                analyzed = analyzed + char
        params = {'purpose': 'Removed Space', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif charcount == "on":
        analyzed = ""
        c = 0
        for char in djtext:
            c += 1
        params = {'purpose': 'Count total no. of characters', 'analyzed_text': 'Total no.of characters = ' + str(c)}
        return render(request, 'analyze.html', params)
    elif extraspaceremover == "on":
        analyzed = ""
        for index,char in enumerate(djtext):
            if djtext[index] == " " and djtext[index + 1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'Extra Spaces Removed', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error!!")

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
