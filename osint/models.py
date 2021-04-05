from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class TruecallerApiKey(models.Model):   
    api_token = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'truecaller_api_key'


class TruecallerDetails(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    birthday =  models.DateField(blank=True, null=True)
    gender =  models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='trucallerImg', max_length=200, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    job_title =  models.CharField(max_length=200, blank=True, null=True)
    company_name = models.CharField(max_length=200, blank=True, null=True)
    carrier = models.CharField(max_length=200, blank=True, null=True)
    street_name = models.CharField(max_length=200, blank=True, null=True)
    zipcode = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    country_code =  models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'truecaller_details'    

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    

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