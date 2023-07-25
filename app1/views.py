from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def one(request):
    return render(request,'one.html')

def two(request):
    return render(request,"two.html")

def string(request):
    return HttpResponse('This is my app1-string as a response')