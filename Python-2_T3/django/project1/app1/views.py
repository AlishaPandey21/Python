from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello World!</h1>")
    
def python(request):
    return HttpResponse("<h1>This is Python Page</h1>")
def php(request):
    return HttpResponse("<h1>This is PHP Page</h1>")
def java(request):
    return HttpResponse("<h1>This is Java Page</h1>")
    
    
    
