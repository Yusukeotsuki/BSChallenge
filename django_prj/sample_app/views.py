from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def input(request):
    return HttpResponse("hello world")
