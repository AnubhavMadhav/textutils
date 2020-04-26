# I have created this file - Anubhav Madhav

from django.http import HttpResponse

def navigate(request):
    nav = '''<h1>Navigate</h1>
    <a href="https://www.linkedin.com/">LinkedIn</a><br>
    <a href="https://twitter.com/">Twitter</a><br>
    <a href="https://github.com/">GitHub</a><br>
    <a href="https://www.facebook.com/">Facebook</a>
    '''
    return HttpResponse(nav)