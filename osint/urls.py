from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('analyse', views.analyse),
    path('iplookup',views.iplookup),
    path('account',views.account),
    path('profile',views.profile),
    path('login',views.login),
    path('logout',views.logout),
    path('case_overview',views.case_overview),
    path('users',views.users),
    path('add_users',views.add_users),
    path('addons',views.addons),
    path('darkwebsearch',views.darkwebsearch),

]