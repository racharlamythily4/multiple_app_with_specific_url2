from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def three(request):
    return render(request,'three.html')

def four(request):
    return render(request,'four.html')

def string(request):
    return HttpResponse('This is my app2-string')