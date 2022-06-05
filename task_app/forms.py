from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User

class signup_form(UserCreationForm):
    password1=forms.CharField(label='Password', widget=forms.PasswordInput)
    password2=forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','email']
        labels={"Email_Address":'email', "UserName":'username'}

class login_form(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput())
    email=UsernameField(widget=forms.EmailInput())
    password=forms.CharField(widget=forms.PasswordInput())