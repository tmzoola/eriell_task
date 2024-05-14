from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(min_length=4, max_length=40, widget=forms.TextInput({"class": "form-control"}))
    email = forms.EmailField(max_length=200,widget=forms.TextInput({"class": "form-control"}))
    password1 = forms.CharField(widget=forms.PasswordInput({"class": "form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput({"class": "form-control"}))

    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2', 'user_role')


class LoginForm(forms.Form):
    username = forms.CharField(min_length=4, max_length=40, widget=forms.TextInput({"class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput({"class": "form-control"}))