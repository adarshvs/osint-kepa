from django.urls import path
from . import views
from .views import users, AddUser

urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('analyse', views.analyse),
    path('iplookup',views.iplookup),
    path('account',views.account),
    path('login',views.login),
    path('logout',views.logout),
    path('case_overview',views.case_overview),
    #path('users',views.users),
    path('add_users',views.add_users),
    path('addons',views.addons),
    path('darkwebsearch',views.darkwebsearch),
    path('users',users.as_view(),name="users"),
    path('add_user/', AddUser.as_view(),name='add_user'),    
    path('edit_profile',views.profileEdit),
    path('change_pass',views.change_password, name='change_password'),

]