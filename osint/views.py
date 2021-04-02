from django.http import HttpResponse
from django.shortcuts import render, redirect
#from osint.includes.classes.truecaller_search_class import Truecaller
import requests
import json
from phonenumbers import carrier
from phonenumbers import geocoder
import phonenumbers
from phonenumbers import timezone
# Create your views here.
def index(request):
    return HttpResponse('OPEN SOUCE INTELLIGENCE GATHERING')
def analyse(request):
    num1 = str(request.POST.get('search'))
    if num1 == 'None':
        num1 = '9048903190'
        token ="Bearer a1i0R--QULj06V5kbAlVPy_aynMfCnoUHbndb2k01j2bzL9nMP1y8Ti1a5o5xNle"
        turl = "https://search5-noneu.truecaller.com/v2/search?q=" + num1 + "&countryCode=IN&type=4&locAddr=&placement=SEARCHRESULTS%2CHISTORY%2CDETAILS&encoding=json"
        theaders = {
                "user-agent": "Truecaller/11.5.7 (Android;10)",
                "Accept-Encoding": "gzip",
                "authorization": token,
                "Host": "search5-noneu.truecaller.com"
            }
        tresponse = requests.get(turl, headers=theaders, timeout=5)
        output = tresponse
        j = output.json()
        name = j['data'][0]['name']
        p = phonenumbers.parse("+91"+num1)
        isp = carrier.name_for_valid_number(p,'en')
        #gender = j['data'][0]['gender']
        return render(request,'analyse.html',{"name":name, "num1":num1, "isp":isp})
    else:
        num1 == num1
        token ="Bearer a1i0R--QULj06V5kbAlVPy_aynMfCnoUHbndb2k01j2bzL9nMP1y8Ti1a5o5xNle"
        turl = "https://search5-noneu.truecaller.com/v2/search?q=" + num1 + "&countryCode=IN&type=4&locAddr=&placement=SEARCHRESULTS%2CHISTORY%2CDETAILS&encoding=json"
        theaders = {
                "user-agent": "Truecaller/11.5.7 (Android;10)",
                "Accept-Encoding": "gzip",
                "authorization": token,
                "Host": "search5-noneu.truecaller.com"
            }
        tresponse = requests.get(turl, headers=theaders, timeout=5)
        output = tresponse
        j = output.json()
        name = j['data'][0]['name']
        p = phonenumbers.parse("+91"+num1)
        isp = carrier.name_for_valid_number(p,'en')
        #gender = j['data'][0]['gender']
        return render(request,'analyse.html',{"name":name, "num1":num1, "isp":isp})
   