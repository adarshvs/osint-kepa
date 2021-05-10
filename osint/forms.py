from django import forms
from django.forms import TextInput, FileInput, NumberInput, Textarea, DateInput, PasswordInput, CheckboxInput, EmailInput
from django.contrib.auth.models import User
from .models import Profile, CaseDetails, MetaFiles
from django.contrib.auth.forms import UserCreationForm

class AddUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'password1', 
            'password2', 
            'is_superuser',
            'is_staff'
            ]

class UserAdminUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','is_superuser','is_staff']
        widgets = {
            "first_name": TextInput(
                attrs={                    
                    "class":"form-control"
                }),
            "last_name": TextInput(
            attrs={                    
                "class":"form-control"
            }),
            "username": TextInput(
            attrs={                    
                "class":"form-control"
            }),       
            
            "email": TextInput(
            attrs={                    
                "class":"form-control"
            })
            
            
            
        }
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email']
        widgets = {
            "first_name": TextInput(
                attrs={                    
                    "class":"form-control"
                }),
            "last_name": TextInput(
            attrs={                    
                "class":"form-control"
            }),
            
            "email": TextInput(
            attrs={                    
                "class":"form-control"
            })
            
            
        }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['designation','profile_pic']
        widgets = {
            
            "profile_pic": FileInput(
                attrs={                    
                    "class":"form-control-file"
                }),
            "designation": TextInput(
                attrs={                    
                    "class":"form-control"
                })}

class PasswordChangeForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['password']
        widgets = {     
            "old_password": TextInput(
                attrs={                    
                    "class":"form-control"
                }),
            "new_password1": TextInput(
            attrs={                    
                "class":"form-control"
            }),
            "new_password2": TextInput(
            attrs={                    
                "class":"form-control"
            })
        }
        

class AddCaseDetailsForm(forms.ModelForm):
    class Meta:
        model = CaseDetails
        fields=['case_details','case_no','ref_id','case_title','fir_date','phone_no','email']
        widgets = {     
            "case_details": Textarea(
                attrs={                    
                    "class":"form-control"
                }),
                            "case_no": TextInput(
                attrs={                    
                    "class":"form-control",
                    "placeholder":"Enter case number* "
                }),
                            "ref_id": TextInput(
                attrs={                    
                    "class":"form-control",
                    "placeholder":"Enter case referance number "
                }),
                
                            "case_title": TextInput(
                attrs={                    
                    "class":"form-control",
                    "placeholder":"Enter case title "
                }),
                
                            "fir_date": DateInput(
                attrs={                    
                    "class":"form-control",
                    "type":"date"
                }),
                
                            "email": EmailInput(
                attrs={                    
                    "class":"form-control",
                    "placeholder":"Enter email "
                }),
                
                            "phone_no": TextInput(
                attrs={                    
                    "class":"form-control",
                    "placeholder":"Enter mobile number without +91"
                })

        }

class MetaFileForm(forms.ModelForm):
    class Meta:
        model = MetaFiles
        fields = ('file_name', )
        widgets = {     
            "file_name": FileInput(
                attrs={                    
                    "class":"custom-file-input",
                    "id":"exampleInputFile"
                })
        }
    
