from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import Profile
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy



from osint.Includes.classes.truecaller_search_class import Truecaller
from osint.Includes.classes.ipapi_class import IpLookup
import requests
import json
from .models import TruecallerApiKey


def profileEdit(request):

    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        u_form = UserUpdateForm(request.POST,instance=request.user)
        if p_form.is_valid() and u_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,'Your Profile has been updated!')
            return redirect(profileEdit)
            
    else:
        p_form = ProfileUpdateForm(instance=request.user)
        u_form = UserUpdateForm(instance=request.user.profile)

    context={'p_form': p_form, 'u_form': u_form}
    return render(request, 'profile_edit.html',context )

    

# Create your views here.
@login_required
def index(request):
    
    user_count = User.objects.all().count()
    return render(request, 'index.html',{'user_count':user_count})
reverse_lazy(index)
        
def login(request):
    if request.user.is_authenticated:
            return redirect(index)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect(index)
        else:
            messages.info(request,'Invalid Credentials')
            return redirect(login)
    else:
        return render(request,'login.html')

class AddUser(CreateView):
    model = User
    template_name = 'add_user.html'
    fields = ('first_name','last_name','username','email','password')
def account(request):
    if not request.user.is_authenticated:
        return redirect(login)

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        admin = request.POST.get('admin', "False")
        staff = request.POST.get('staff', "False")
        if admin == 'on':
            admin = 'True'
        if staff == 'on':
            staff = 'True'
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
               
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')               
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name, is_superuser=admin, is_staff=staff)
                user.save()
                messages.info(request,'user added')
                return redirect(account)
        else:
            messages.info(request,'Password not matching') 
                       
        return redirect(account)
    else:
        return render(request,'account.html')
@login_required
def profile(request):
    
    return render(request,'profile.html')

def analyse(request):
    if not request.user.is_authenticated:
        return redirect(login)
    #key = TruecallerApiKey.objects.all()
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
        return render(request,'analyse.html',{"name":name, "num1":num1, "carrier":carrier, "email":email,"gender":gender,"street":street,"city":city,"image":image})

def iplookup(request):
    if not request.user.is_authenticated:
        return redirect(login)
    ip = str(request.POST.get('search'))
    if ip == 'None':
        return render(request,'iplookup.html')
    else:
        ip_details = IpLookup(ip)
        output = ip_details.ip_lookup()
        data = output.json()
        return render(request,'iplookup.html',{"data":data})


def logout(request):
    auth.logout(request)
    return redirect(login)


def case_overview(request):
    if not request.user.is_authenticated:
        return redirect(login)
    return render(request,'case_overview.html')

class users(LoginRequiredMixin, ListView):
    login_url = '/osint/login'
    redirect_field_name = ''
    model = User
    template_name = 'users.html'
    

def add_users(request):
    if not request.user.is_authenticated:
        return redirect(login)
    return render(request,'add_users.html')

def addons(request):
    if not request.user.is_authenticated:
        return redirect(login)
    return render(request,'addons.html')


def darkwebsearch(request):
    if not request.user.is_authenticated:
        return redirect(login)
    return render(request,'darkwebsearch.html')




