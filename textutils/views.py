# I have created this file - Anubhav Madhav

from django.http import HttpResponse


def index(request):
    home = '''<h1> Home <h1>
    <a href="http://127.0.0.1:8000/removepunc">Remove Punctuations</a><br>
    <a href="http://127.0.0.1:8000/capitalizefirst">Capitalize First</a><br>
    <a href="http://127.0.0.1:8000/newlineremove">Remove New Line</a><br>
    <a href="http://127.0.0.1:8000/spaceremove">Remove Space</a><br>
    <a href="http://127.0.0.1:8000/charcount">Count Characters</a><br>
    '''
    return HttpResponse(home)

def navigate(request):
    nav = '''<h1>Navigate</h1>
    <a href="https://www.linkedin.com/">LinkedIn</a><br>
    <a href="https://twitter.com/">Twitter</a><br>
    <a href="https://github.com/">GitHub</a><br>
    <a href="https://www.facebook.com/">Facebook</a>
    '''
    return HttpResponse(nav)


def removepunc(request):
    a = '''<h1>Remove Punctuations</h1>
    <a href="http://127.0.0.1:8000/" ><button>Home</button></a>
    '''
    return HttpResponse(a)

def capitalizefirst(request):
    b = '''<h1>Capitalize First</h1>
    <a href="http://127.0.0.1:8000/" ><button>Home</button></a>
    '''
    return HttpResponse(b)


def newlineremove(request):
    c = '''<h1>Remove New Line</h1>
    <a href="http://127.0.0.1:8000/" ><button>Home</button></a>
    '''
    return HttpResponse(c)


def spaceremove(request):
    d = '''<h1>Remove Space</h1>
    <a href="http://127.0.0.1:8000/" ><button>Home</button></a>
    '''
    return HttpResponse(d)


def charcount(request):
    e = '''<h1>Count Characters</h1>
    <a href="http://127.0.0.1:8000/" ><button>Home</button></a>
    '''
    return HttpResponse(e)

