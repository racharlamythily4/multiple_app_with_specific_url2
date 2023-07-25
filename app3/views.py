from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def five(request):
    return render(request,'five.html')

def six(request):
    return render(request,'six.html')

def string(request):
    return HttpResponse('This is my app3-string')
    