from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def virat(request):
    return HttpResponse('<h1>capitan of rcb will lift the trophy this year</h1>')