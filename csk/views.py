from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def ruturaj(request):
    return HttpResponse('<h1>Ruturaj is the captain of csk</h1>')