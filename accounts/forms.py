from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms
class CustomRegister(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username','password1', 'password2']
