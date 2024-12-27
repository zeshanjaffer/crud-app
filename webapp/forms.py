from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput , TextInput

from django import forms
from .models import Record

# -Register a user
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username','password1','password2']
        
class LoginForm(AuthenticationForm):
    username =forms.CharField(widget=TextInput())  
    password = forms.CharField(widget=PasswordInput())
    
    
class CreateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields =['first_name','last_name','email','phone','address','city','province','country']
            
            
class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields =['first_name','last_name','email','phone','address','city','province','country']
         