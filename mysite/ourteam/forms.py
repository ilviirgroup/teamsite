from django import forms
from .models import User
from django.contrib.auth.forms import AuthenticationForm



class UserLoginForm(AuthenticationForm):
    user_name = forms.CharField(label='User name', widget=forms.TextInput(attrs={'class': 'form-control'})),
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'})),



class UserForm(forms.ModelForm):
    user_name = forms.CharField(label='User name', widget=forms.TextInput(attrs={'class': 'form-control'})),
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': 'form-control'})),
    surname = forms.CharField(label='Surname', widget=forms.TextInput(attrs={'class': 'form-control'})),
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'})),
    email = forms.CharField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'})),
    num = forms.CharField(label='Phone', widget=forms.TextInput(attrs={'class': 'form-control'})),
    group = forms.CharField(label='Group', widget=forms.Select(attrs={'class': 'form-control'})),

    class Meta:
        model = User
        fields = ['user_name', 'name', 'surname', 'password', 'email', 'num', 'group']


