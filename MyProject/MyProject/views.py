from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'Home.html')

def about(request):
    return render(request, 'about.html')