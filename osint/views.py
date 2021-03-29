from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return HttpResponse('OPEN SOUCE INTELLIGENCE GATHERING')
def analyse(request):
    return render(request,'analyse.html')