from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index1(request):
    return HttpResponse('<h1 style="color: red; text-align: center;">Primera vista APP1</h1>')


def index2(request):
    return HttpResponse('<h1 style="color: red; text-align: center;">Segunda vista APP1</h1>')
