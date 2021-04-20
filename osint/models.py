from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

from django.conf import settings

from django.core.validators import RegexValidator

from django_currentuser.middleware import (get_current_user, get_current_authenticated_user)
# As model field:
from django_currentuser.db.models import CurrentUserField

class TruecallerApiKey(models.Model):   
    api_token = models.CharField(max_length=200, unique=True)
    is_active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'truecaller_api_keys'
class EyeconApiKey(models.Model):   
    api_token = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'eyecon_api_keys'


class CaseDetails(models.Model):
    
    case_no = models.CharField(max_length=200, unique=True )
    ref_id = models.CharField(max_length=200 )
    case_title = models.CharField(max_length=200)
    case_details = models.TextField(blank=True, null=True)
    fir_date = models.DateField()
    email = models.CharField(max_length=200 , blank=True, null=True)
    phone_regex = RegexValidator(regex=r'^\d{10}$', message="Phone number must be entered without +91. Up to 10 digits allowed.")
    phone_no = models.CharField(validators=[phone_regex],max_length=200 , blank=True, null=True)
    analysis_status = models.BooleanField(default='False')
    is_completed = models.BooleanField(default='False')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = CurrentUserField()
    
    def get_absolute_url(self):
        return reverse('analyse')
    class Meta:
        db_table = 'case_details'
        ordering = ['-created_at']

class TruecallerDetails(models.Model):
    case_no = models.IntegerField()
    name = models.CharField(max_length=200, blank=True, null=True)
    email =  models.EmailField(blank=True, null=True)
    carrier =  models.CharField(max_length=200, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=200, blank=True, null=True)    
    gender =  models.CharField(max_length=200, blank=True, null=True)
    street = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    address = models.TextField(max_length=200, blank=True, null=True)
    birthday = models.TextField(max_length=200, blank=True, null=True)
    jobTitle = models.CharField(max_length=200, blank=True, null=True)
    companyName =  models.CharField(max_length=200, blank=True, null=True)
    created_by = CurrentUserField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'truecaller_details'    

class EyeconDetails(models.Model):
    case_no = models.IntegerField()
    suspects_name = models.CharField(max_length=200, blank=True, null=True)
    image = models.CharField(max_length=1000, blank=True, null=True)  
    created_by = CurrentUserField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'eyecon_details'      

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    enable_dark = models.BooleanField(default='False')
    designation = models.CharField(max_length=200, blank=True, null=True)
    profile_pic = models.ImageField(upload_to="avatars/",default="avatars/user.jpg", max_length=200, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



class IpLookupData(models.Model):
    ip = models.CharField(max_length=200, blank=True, null=True)    
    version =  models.CharField(max_length=200, blank=True, null=True)
    city =  models.CharField(max_length=200, blank=True, null=True)
    region =  models.CharField(max_length=200, blank=True, null=True)
    region_code =  models.CharField(max_length=200, blank=True, null=True)
    country_name =  models.CharField(max_length=200, blank=True, null=True)
    country_code =  models.CharField(max_length=200, blank=True, null=True)
    country_code_iso3 =  models.CharField(max_length=200, blank=True, null=True)
    country_capital =  models.CharField(max_length=200, blank=True, null=True)
    country_tld =  models.CharField(max_length=200, blank=True, null=True)
    continent_code =  models.CharField(max_length=200, blank=True, null=True)
    in_eu =  models.CharField(max_length=200, blank=True, null=True)
    postal =  models.CharField(max_length=200, blank=True, null=True)
    latitude =  models.CharField(max_length=200, blank=True, null=True)
    longitude =  models.CharField(max_length=200, blank=True, null=True)
    timezone =  models.CharField(max_length=200, blank=True, null=True)
    utc_offset =  models.CharField(max_length=200, blank=True, null=True)
    country_calling_code =  models.CharField(max_length=200, blank=True, null=True)
    currency_name =  models.CharField(max_length=200, blank=True, null=True)
    languages =  models.CharField(max_length=200, blank=True, null=True)
    country_area =  models.CharField(max_length=200, blank=True, null=True)
    country_population =  models.CharField(max_length=200, blank=True, null=True)
    asn =  models.CharField(max_length=200, blank=True, null=True)
    org =  models.CharField(max_length=200, blank=True, null=True)
    currency =  models.CharField(max_length=200, blank=True, null=True)
    created_by = CurrentUserField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'iplookup_data'   
