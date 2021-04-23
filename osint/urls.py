from django.urls import path
from . import views
from .views import users, AddUser, AddCaseDetails, ViewAllCases, ViewCasesDetails, ViewUser, DeleteUser, UserProfileUpdate, AdminUserProfileUpdate, UpdateCaseStatus, UpdateTheme, AddTruecallerApi, ViewAllTruecallerApi, AllUpiLists

urlpatterns = [
    path('', views.index),
    path('index', views.index,name='index'),
    #path('<int:pk>/truecaller/', views.truecaller, name='truecaller'),    
    path('<int:pk>/startanalyse/', views.startAnalyse, name='startanalyse'),
    path('iplookup',views.iplookup),
    path('account',views.account, name= 'account'),
    path('login',views.login),
    path('logout',views.logout),
    path('case_overview', ViewAllCases.as_view(), name='case_overview'),
    path('<int:pk>/case_details/', ViewCasesDetails.as_view(), name='case_details'),
    path('<int:pk>/mycases/', views.mycases, name='mycases'),
    path('addons',views.addons),
    path('darkwebsearch',views.darkwebsearch),
    path('users',users.as_view(),name="users"),
    path('add_user/', AddUser.as_view(),name='add_user'),    
    path('<int:pk>/edit_profile',UserProfileUpdate.as_view(), name= 'edit_profile'),
    path('analyse', AddCaseDetails.as_view(), name='analyse'),
    path('<int:pk>/profile/', ViewUser.as_view(), name='view-profile'),
    path('<int:pk>/delete/', DeleteUser.as_view(), name='delete-profile'),
    path('<int:pk>/update/', AdminUserProfileUpdate.as_view(), name='update-profile'),
    path('<int:pk>/update-case-status/', UpdateCaseStatus.as_view(), name='update-case-status'),
    path('<int:pk>/updatetheme/', UpdateTheme.as_view(), name='update-theme'),
    path('change_pass',views.change_password, name='change_password'),
    path('add-api/', AddTruecallerApi.as_view(), name='add-api'),
    path('truecaller-api/', ViewAllTruecallerApi.as_view(), name='truecaller-api'),
    path('settings/', AllUpiLists.as_view(), name='settings'),
]