from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Count

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User, auth
from .models import Profile, CaseDetails, IpLookupData, TruecallerDetails, TruecallerApiKey, EyeconDetails, UpiLists, EyeconApiKey, UpiDetails
from django.contrib import messages
from django.views import generic

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from .forms import UserUpdateForm,ProfileUpdateForm, PasswordChangeForm, AddCaseDetailsForm, AddUserForm, UserAdminUpdateForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test

from osint.Includes.classes.truecaller_search_class import Truecaller
from osint.Includes.classes.eyecon import Eyecon
from osint.Includes.classes.upi_validator_class import UpiValidator

from osint.Includes.classes.ipapi_class import IpLookup
import requests
import json



# Create your views here.
@login_required
def index(request):
    
    user_count = User.objects.all().count()
    cases_count = CaseDetails.objects.all().count()
    pendig_casecount = CaseDetails.objects.filter(is_completed=False).count()
    completed_cases = CaseDetails.objects.filter(is_completed=True).count()

    mycases_count =  CaseDetails.objects.filter(created_by=request.user).count()
    mycases_pendig_casecount = CaseDetails.objects.filter(created_by=request.user, is_completed=False).count()
    mycases_completed_cases = CaseDetails.objects.filter(created_by=request.user, is_completed=True).count()
    last_ten = CaseDetails.objects.filter(created_by=request.user).order_by('-id')[:5]
   # last_ten_in_ascending_order = reversed(last_ten)
    top_ten = CaseDetails.objects.all().order_by('-id')[:5]
   # top_ten_in_ascending_order = reversed(last_ten)
    context = {'user_count':user_count,"cases_count":cases_count,"pendig_casecount":pendig_casecount, "completed_cases":completed_cases,"mycases_count":mycases_count,"mycases_completed_cases":mycases_completed_cases,"mycases_pendig_casecount":mycases_pendig_casecount,"last_ten":last_ten,"top_ten":top_ten}
    return render(request, 'index.html',context)
reverse_lazy(index)
@login_required
def mycases(request, pk):
    case_details =  CaseDetails.objects.filter(created_by=request.user)
    return render(request, 'mycases.html',{"case_details":case_details})
        
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
def change_password(request):
    if request.method == 'POST':
        pass_form = PasswordChangeForm(request.user, request.POST)
        if pass_form.is_valid():
            user = pass_form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        pass_form = PasswordChangeForm(request.user)
    return render(request, 'profile/change_password.html', {
        'pass_form': pass_form
    })
def startAnalyse(request, pk):
    case_no = pk
    emails = CaseDetails.objects.values_list('email', flat=True).filter(id=pk)
    for email in emails:
        email = email
    phone_nos =  CaseDetails.objects.values_list('phone_no', flat=True).filter(id=pk)
    for phone_no in phone_nos:
        phone_no = phone_no
    if phone_no:
        token_truecaller ="Bearer a1i0R--QULj06V5kbAlVPy_aynMfCnoUHbndb2k01j2bzL9nMP1y8Ti1a5o5xNle"
        token_eyecon ="c4664ab6-6202-4bb2-8ac5-dbd8bfbd5861"
        if TruecallerDetails.objects.filter(case_no = pk).exists():
            messages.info(request, ' Trucaller OSINT related with this case number already completed')
        else:
            true_caller_result = Truecaller(phone_no, token_truecaller)
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
                street = "unknown"
            try:
                city = j['data'][0]['addresses'][0]['city']
            except KeyError:
                city = "unknown"
            try:
                address = j['data'][0]['addresses'][0]['address']
            except KeyError:
                address = "unknown"
            
            try:
                image = j['data'][0]['image']
            except KeyError:
                image = "not known"
            try:
                birthday = j['data'][0]['birthday']
            except KeyError:
                birthday = "unknown"
            try:
                jobTitle = j['data'][0]['jobTitle']
            except KeyError:
                jobTitle = "unknown"
            try:
                companyName = j['data'][0]['companyName']
            except KeyError:
                companyName = "unknown"
            try:
                about = j['data'][0]['about']
            except KeyError:
                about = "unknown"
            
            truecaller_data = TruecallerDetails(name=name, email=email, carrier=carrier, about=about,image=image,gender=gender, street=street, city=city, address=address, birthday=birthday, jobTitle=jobTitle, companyName=companyName,case_no=case_no)
            truecaller_data.save()
            messages.success(request, 'Truecaller OSINT Completed')
        if EyeconDetails.objects.filter(case_no = pk).exists():
            messages.info(request, ' Eyecon OSINT related with this case number already completed')
        else:
            eyecon_result = Eyecon(phone_no, token_eyecon)
            eyecon_resp = eyecon_result.eyecon_search()
            eyecon_json = eyecon_resp.json()
            temp = json.dumps(eyecon_json).replace('[', '').replace(']', '')
            jsonload = json.loads(temp)
            name_eyecon =  jsonload["name"]
            imgresp = eyecon_result.eyecon_img_search()
            img_split = imgresp.url.replace('https://graph.', '').replace('picture?width=600', '')
            img_http_resp = requests.get(img_split)
            if not img_http_resp.status_code == 200:
                img_path = "None"
            else:
                img_path = img_split
            eyecon_data = EyeconDetails(suspects_name= name_eyecon, image=img_path,case_no=case_no)
            eyecon_data.save()
            messages.success(request, 'Eyecon OSINT Completed')
        if UpiDetails.objects.filter(vpa_id = phone_no).exists():
            messages.info(request, 'Already Found all possible upi addresses of this mobile number')
        else:
            upix = UpiLists.objects.all().values_list('upi_id', flat=True)
            upi1 = upix[::1]
            vpa = phone_no #text before @ symbol
            for upi in upi1:    
                UpiValidator_result = UpiValidator(vpa, upi)
                output = UpiValidator_result.VpaValidator()
                upi_res1 = output.json()
                upi_res_status = upi_res1['status']
                if upi_res_status == str('VALID'):
                    upi_res = upi_res1['customer_name']
                    vpax =  upi_res1['vpa']
                    vpa_addrs = vpax.partition('@')[2]
                    upi_data = UpiDetails(name = upi_res, vpa = vpax, case_no=case_no, vpa_id = vpa, bank= vpa_addrs)
                    upi_data.save()
            messages.success(request, 'UPI OSINT of the particular mobile number Completed')
        a = CaseDetails.objects.get(id = pk )
        a.analysis_status = 'True'
        a.save()
        messages.success(request, 'Case staus updated')
    else:
        messages.error(request, 'No mobile numbers were found associated with this case')
    if email:
        if UpiDetails.objects.filter(vpa_id = email).exists():
            messages.info(request, 'Already Found all possible upi addresses of this email address')
        else:
            upix = UpiLists.objects.all().values_list('upi_id', flat=True)
            upi1 = upix[::1]
            email_uname = email.partition('@')[0]
            vpa = email_uname #text before @ symbol
            for upi in upi1:    
                UpiValidator_result = UpiValidator(vpa, upi)
                output = UpiValidator_result.VpaValidator()
                upi_res1 = output.json()
                upi_res_status = upi_res1['status']
                if upi_res_status == str('VALID'):
                    upi_res = upi_res1['customer_name']
                    vpax =  upi_res1['vpa']
                    vpa_addrs = vpax.partition('@')[2]
                    upi_data = UpiDetails(name = upi_res, vpa = vpax, case_no=case_no, vpa_id = vpa, bank= vpa_addrs)
                    upi_data.save()
            messages.success(request, 'UPI OSINT of the particular email id Completed')
    else:
        messages.error(request, 'No email addresses were found associated with this case')
    return redirect(request.META['HTTP_REFERER'])
def iplookup(request):
    if not request.user.is_authenticated:
        return redirect(login)
    ip = str(request.POST.get('search'))
    ip_count= IpLookupData.objects.distinct('ip') 
    if ip == 'None':

        return render(request,'iplookup.html',{"ip_count":ip_count})
    else:
        ip_details = IpLookup(ip)
        output = ip_details.ip_lookup()
        data = output.json()
        try:
            ip = data['ip']
        except KeyError:
            ip = "not known"
        try:
            version = data['version']
        except KeyError:
            version = "unknown"
        try:
            city = data['city']
        except KeyError:
            city = "unknown"
        try:
            region = data['region']
        except KeyError:
            region = "unknown"
        try:
            region_code = data['region_code']
        except KeyError:
            region_code = "unknown"
        try:
            country = data['country']
        except KeyError:
            country = "unknown"
        try:
            country_name = data['country_name']
        except KeyError:
            country_name = "unknown"        
        try:
            country_code = data['country_code']
        except KeyError:
            country_code = "unknown"  
        try:
            country_code_iso3 = data['country_code_iso3']
        except KeyError:
            country_code_iso3 = "unknown" 
        try:
            country_capital = data['country_capital']
        except KeyError:
            country_capital = "unknown" 
        try:
            country_tld = data['country_tld']
        except KeyError:
            country_tld = "unknown" 
        continent_code = data['continent_code']
        in_eu = data['in_eu']
        postal = data['postal']
        #if latitude == str('Sign up to access'):
         #   latitude = "N/A"
         #   longitude = "N/A"
        latitude = data['latitude']
        longitude = data['longitude']
            
        timezone = data['timezone']
        utc_offset = data['utc_offset']
        country_calling_code = data['country_calling_code']
        currency = data['currency']
        currency_name = data['currency_name']
        languages = data['languages']
        country_area = data['country_area']
        country_population = data['country_population']
        asn = data['asn']
        org = data['org']


        ip_data = IpLookupData(ip=ip, version = version, city=city, region=region, region_code = region_code, country_name = country_name,country_code = country_code, country_code_iso3 = country_code_iso3, country_capital =country_capital, country_tld= country_tld, continent_code = continent_code, in_eu=in_eu, postal = postal,latitude = latitude, longitude = longitude,timezone = timezone, utc_offset = utc_offset, country_calling_code = country_calling_code, currency = currency,currency_name = currency_name, languages= languages, country_area= country_area, country_population = country_population, asn= asn, org= org)
        #model = IpLookup
        ip_data.save()
        ip_count= IpLookupData.objects.distinct('ip') 
        context = {"ip":ip,"version":version,"city":city,"region":region,"region_code":region_code,"country":country,"country_name":country_name,"country_code":country_code,"country_code_iso3":country_code_iso3,"country_capital":country_capital,"country_tld":country_tld,"continent_code":continent_code,"in_eu":in_eu,"postal":postal,"latitude":latitude,"longitude":longitude,"timezone":timezone,"utc_offset":utc_offset,"country_calling_code":country_calling_code,"currency":currency,"currency_name":currency_name,"languages":languages,"country_area":country_area,"country_population":country_population,"asn":asn,"org":org,"data":data,"ip_count":ip_count}
        
        return render(request,'iplookup.html',context)


def logout(request):
    auth.logout(request)
    return redirect(login)




    


def addons(request):
    if not request.user.is_authenticated:
        return redirect(login)
    return render(request,'addons.html')


def darkwebsearch(request):
    if not request.user.is_authenticated:
        return redirect(login)
    
    return render(request,'darkwebsearch.html')

@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')  
class users(ListView):
    
    model = User
    template_name = 'users.html'

@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')  
class AddUser(SuccessMessageMixin, CreateView):
    form_class = AddUserForm
    template_name = 'profile/add_user.html'
    success_url = reverse_lazy('users')
    success_message = "%(username)s is created successfully"


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')    
class ViewUser(DetailView):
    model = User
    fields = '__all__'
    template_name = 'profile/viewuser.html'
    context_object_name = 'userp'


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')    
class DeleteUser(DeleteView):
    model = User
    context_object_name = 'userp'
    template_name = 'profile/delete.html'
    success_url = reverse_lazy('users')

@method_decorator(login_required, name='dispatch')
class AddCaseDetails(SuccessMessageMixin, generic.CreateView):
    form_class = AddCaseDetailsForm
    model = CaseDetails
    template_name = 'add_case_details.html'
    success_url = reverse_lazy('index')    
    success_message = 'Case details added successfully. You may now start osint analysis under My Case History tab'

@method_decorator(login_required, name='dispatch')
class ViewAllCases(generic.ListView):
    
    model = CaseDetails
    template_name = 'case_overview.html'



@method_decorator(login_required, name='dispatch')
class ViewCasesDetails(generic.TemplateView):
    template_name = 'case_details.html'
    def get_context_data(self, **kwargs):
         pk = int(kwargs['pk'])
         context = super(ViewCasesDetails, self).get_context_data(**kwargs)
         context['casedetails'] = CaseDetails.objects.filter(id=pk)
         context['truecallerdetails'] = TruecallerDetails.objects.filter(case_no=pk)
         context['eycondetails'] = EyeconDetails.objects.filter(case_no=pk)
         context['upidetails'] = UpiDetails.objects.filter(case_no=pk)         
         context['upidetails_uniquename'] = UpiDetails.objects.filter(case_no=pk).distinct('name')
         context['upidetails_uniquevpa'] = UpiDetails.objects.filter(case_no=pk).distinct('vpa')
         return context

@method_decorator(login_required, name='dispatch')
class UserProfileUpdate(SuccessMessageMixin, UpdateView):
    
    model = Profile
    template_name = 'profile/updateuser.html'
    form_class = ProfileUpdateForm
    second_form_class = UserUpdateForm
    success_message = 'profile updated successfully'
    success_url = reverse_lazy('change_password')

    def get_context_data(self, **kwargs):
        context = super(UserProfileUpdate, self).get_context_data(**kwargs)

        context['user_form'] = self.second_form_class(self.request.POST or None, instance=self.object.user)

        return context
    

    def form_valid(self, form):
        user_form = UserUpdateForm(self.request.POST, instance=self.object.user)
        if user_form.is_valid():
            user_form.save()
        return super(UserProfileUpdate, self).form_valid(form)

@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')    
class AdminUserProfileUpdate(SuccessMessageMixin, UpdateView):
    
    model = Profile
    template_name = 'profile/admin-updateuser.html'
    form_class = ProfileUpdateForm
    second_form_class = UserAdminUpdateForm
    success_message = 'profile updated successfully'
    success_url = reverse_lazy('users')

    def get_context_data(self, **kwargs):
        context = super(AdminUserProfileUpdate, self).get_context_data(**kwargs)

        context['user_form'] = self.second_form_class(self.request.POST or None, instance=self.object.user)

        return context
    

    def form_valid(self, form):
        user_form = UserAdminUpdateForm(self.request.POST, instance=self.object.user)
        if user_form.is_valid():
            user_form.save()
        return super(AdminUserProfileUpdate, self).form_valid(form)

@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')    
class UpdateCaseStatus(UpdateView):
    model = CaseDetails
    fields = ["is_completed"]    
    template_name = 'updatecasestatus.html'
    success_url = reverse_lazy('case_overview')

@method_decorator(login_required, name='dispatch')
class UpdateTheme(UpdateView):
    model = Profile
    fields = ["enable_dark"]    
    template_name = 'theme/updatetheme.html'
    success_url = reverse_lazy('index')

@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch') 
class AllUpiLists(generic.TemplateView):
    template_name = 'settings/settings.html'
    def get_context_data(self, **kwargs):
         context = super(AllUpiLists, self).get_context_data(**kwargs)
         context['upilists'] = UpiLists.objects.all()
         context['truecallerapi'] = TruecallerApiKey.objects.all()
         context['eyeconapi'] = EyeconApiKey.objects.all()
         return context

@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')    
class AddUpi(SuccessMessageMixin, generic.CreateView):
    model = UpiLists
    fields = ["upi_id","bank_name"]
    template_name = 'settings/add_upi.html'
    success_url = reverse_lazy('settings')    
    success_message = 'New UPI added to the database'

@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')    
class UpdateUpi(SuccessMessageMixin, UpdateView):
    model = UpiLists
    fields = ["upi_id","bank_name"]    
    template_name = 'settings/update_upi.html'
    success_url = reverse_lazy('settings')    
    success_message = ' UPI details updated successfully'

@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')    
class DeleteUpi(SuccessMessageMixin, DeleteView):
    model = UpiLists
    template_name = 'settings/delete_upi.html'
    success_url = reverse_lazy('settings')    
    success_message = ' UPI deleted successfully'


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')    
class AddTruecallerToken(SuccessMessageMixin, generic.CreateView):
    model = TruecallerApiKey
    fields = ["api_token","is_active"]
    template_name = 'settings/add_truecaller_api.html'
    success_url = reverse_lazy('settings')    
    success_message = 'New Truecaller authorization token added to the database'

@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')    
class AddEyeconToken(SuccessMessageMixin, generic.CreateView):
    model = EyeconApiKey
    fields = ["api_token","is_active"]
    template_name = 'settings/add_eyecon_api.html'
    success_url = reverse_lazy('settings')    
    success_message = 'New Eyecon authorization token added to the database'