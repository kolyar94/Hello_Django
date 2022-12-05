from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    a = 5+6
    return render(request,'about.html',{'gretting':a})

def home(reqest):
    return HttpResponse('This is my home')