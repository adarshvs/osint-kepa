from django.http import HttpResponse
from django.shortcuts import render, redirect
from osint.Includes.classes.truecaller_search_class import Truecaller
import requests
import json
from phonenumbers import carrier
from phonenumbers import geocoder
import phonenumbers
from phonenumbers import timezone
from .models import TruecallerApiKey
# Create your views here.
def index(request):
    return HttpResponse('OPEN SOUCE INTELLIGENCE GATHERING')
def analyse(request):
    key = TruecallerApiKey.objects.all()
    num1 = str(request.POST.get('search'))
    token ="Bearer a1i0R--QULj06V5kbAlVPy_aynMfCnoUHbndb2k01j2bzL9nMP1y8Ti1a5o5xNle"
    if num1 == 'None':
        return render(request,'analyse.html')
    else:        
        num1 == num1
        true_caller_result = Truecaller(num1, token)
        output = true_caller_result.truecaller_search()
        j = output.json()
        name = j['data'][0]['name']
        if j['data'][0]['internetAddresses']:
            email = j['data'][0]['internetAddresses'][0]['id']
        elif not j['data'][0]['internetAddresses']:
            email = "not available"
        try:
            carrier = j['data'][0]['phones'][0]['carrier']
        except KeyError:
            carrier = "not available"
        try:
            gender = j['data'][0]['gender']
        except KeyError:
            gender = "gender is unknown"
        try:
            street = j['data'][0]['addresses'][0]['street']
        except KeyError:
            street = "not known"
        city = j['data'][0]['addresses'][0]['city']
        try:
            image = j['data'][0]['image']
        except KeyError:
            image = "not known"
        return render(request,'analyse.html',{"name":name, "num1":num1, "carrier":carrier, "email":email,"gender":gender,"street":street,"city":city,"key":key,"image":image})
    
   