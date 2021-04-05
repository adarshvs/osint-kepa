from django import forms
from django.forms import TextInput, FileInput
from django.contrib.auth.models import User
from .models import Profile

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email']
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
        



