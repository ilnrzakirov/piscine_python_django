from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Tip


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class TipForm(forms.ModelForm):
    class Meta:
        model = Tip
        fields = ['content']
