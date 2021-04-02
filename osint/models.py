from django.db import models


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
        abstract = True