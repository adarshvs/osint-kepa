from django.contrib import admin
from .models import TruecallerApiKey
from .models import TruecallerDetails
from .models import Profile, CaseDetails
# Register your models here.

admin.site.register(TruecallerApiKey)
admin.site.register(TruecallerDetails)
admin.site.register(Profile)
admin.site.register(CaseDetails)