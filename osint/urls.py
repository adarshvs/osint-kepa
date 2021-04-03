from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('analyse', views.analyse),
    path('iplookup',views.iplookup),
    path('account',views.account)
]