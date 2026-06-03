from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request,'about.html')
def course(request):
    return render(request,'course.html')
def home(request):
    return render(request,'home.html')
def java(request):
    return render(request,'java.html')
def python(request):
    return render(request,'python.html')