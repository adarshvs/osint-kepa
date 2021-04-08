from django.urls import path
from . import views
from .views import users, AddUser, AddCaseDetails, ViewAllCases, ProfileUpdate, ViewCasesDetails, ViewUser, DeleteUser, UpdateUser

urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('truecaller', views.truecaller, name='truecaller'),
    path('iplookup',views.iplookup),
    path('account',views.account, name= 'account'),
    path('login',views.login),
    path('logout',views.logout),
    path('case_overview', ViewAllCases.as_view(), name='case_overview'),
    path('<int:pk>/case_details/', ViewCasesDetails.as_view(), name='case_details'),
    #path('users',views.users),
    #path('add_users',views.add_users),
    path('addons',views.addons),
    path('darkwebsearch',views.darkwebsearch),
    path('users',users.as_view(),name="users"),
    path('add_user/', AddUser.as_view(),name='add_user'),    
    path('edit_profile',views.profileEdit),
    path('change_pass',views.change_password, name='change_password'),
    path('analyse', AddCaseDetails.as_view(), name='analyse'),
    path('profile/update', ProfileUpdate.as_view(), name='update_profile'),
    path('<int:pk>/profile/', ViewUser.as_view(), name='view-profile'),
    path('<int:pk>/delete/', DeleteUser.as_view(), name='delete-profile'),
    path('<int:pk>/update/', UpdateUser.as_view(), name='update-profile'),

]