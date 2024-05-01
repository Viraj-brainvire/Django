from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email=forms.EmailField()
    firs_name=forms.CharField()
    last_name=forms.CharField()
    