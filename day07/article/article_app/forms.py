from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Article


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class ArticleForm(forms.ModelForm):
    synopsis = forms.CharField(max_length=300, widget=forms.Textarea)

    class Meta:
        model = Article
        fields = ('title', 'synopsis', 'content')


class AddForm(forms.Form):
    title = forms.ChoiceField(choices=(), required=True)

    def __init__(self, choices, *args, **kwargs):
        super(AddForm, self).__init__(*args, **kwargs)
        self.fields['title'].choices = choices
