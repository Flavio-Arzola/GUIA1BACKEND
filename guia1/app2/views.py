from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("View Numero 1")

def index2(request):
    return HttpResponse("View Numero 2")

# Create your views here.
