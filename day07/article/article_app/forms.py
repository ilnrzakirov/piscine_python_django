from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Article


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'synopsis', 'content')
