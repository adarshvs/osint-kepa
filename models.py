# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CaseDetails(models.Model):
    username = models.CharField(max_length=255, blank=True, null=True)
    case_name = models.CharField(max_length=255, blank=True, null=True)
    ref_no = models.CharField(max_length=255, blank=True, null=True)
    case_details = models.CharField(max_length=500, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'case_details'


class EmailOsint(models.Model):
    fb_url = models.CharField(max_length=255, blank=True, null=True)
    twitter_url = models.CharField(max_length=200, blank=True, null=True)
    instagram_url = models.CharField(max_length=200, blank=True, null=True)
    other_url = models.CharField(max_length=200, blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'email_osint'


class GmailDetails(models.Model):
    owner_name = models.CharField(max_length=200, blank=True, null=True)
    goolge_id = models.CharField(max_length=200, blank=True, null=True)
    google_services = models.CharField(max_length=200, blank=True, null=True)
    youtube_channel = models.CharField(max_length=200, blank=True, null=True)
    map_contributions = models.CharField(max_length=200, blank=True, null=True)
    calendar_events = models.CharField(max_length=200, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gmail_details'


class MobOsint(models.Model):
    name_truecaller = models.CharField(max_length=200, blank=True, null=True)
    name_eyecon = models.CharField(max_length=200, blank=True, null=True)
    name_fb = models.CharField(max_length=200, blank=True, null=True)
    mail_id = models.CharField(max_length=255, blank=True, null=True)
    fb_url = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    msp = models.CharField(max_length=200, blank=True, null=True)
    upi_id = models.CharField(max_length=200, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mob_osint'


class TruecallerApiKey(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    api_token = models.CharField(max_length=200, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'truecaller_api_key'


class TruecallerDetails(models.Model):
    owner_name = models.CharField(max_length=200, blank=True, null=True)
    gender = models.CharField(max_length=200, blank=True, null=True)
    about = models.CharField(max_length=500, blank=True, null=True)
    job_title = models.CharField(max_length=200, blank=True, null=True)
    company_name = models.CharField(max_length=200, blank=True, null=True)
    e164_format = models.CharField(max_length=200, blank=True, null=True)
    national_format = models.CharField(max_length=200, blank=True, null=True)
    dialing_code = models.CharField(max_length=200, blank=True, null=True)
    country_code = models.CharField(max_length=200, blank=True, null=True)
    carrier_name = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    street = models.CharField(max_length=200, blank=True, null=True)
    zip_code = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    country_code2 = models.CharField(max_length=200, blank=True, null=True)
    time_zone = models.CharField(max_length=200)
    internet_addresses_id = models.CharField(max_length=200, blank=True, null=True)
    internet_addresses_service = models.CharField(max_length=200)
    internet_addresses_caption = models.CharField(max_length=200, blank=True, null=True)
    is_user = models.CharField(max_length=200, blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'truecaller_details'


class User(models.Model):
    f_name = models.CharField(max_length=255, blank=True, null=True)
    l_name = models.CharField(max_length=255, blank=True, null=True)
    dob = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=10, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    profile_pic = models.CharField(max_length=200, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
