from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError

from .models import *


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sect'].empty_label = "Категория не выбрана"

    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'photo', 'status', 'sect']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'body': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 100:
            raise ValidationError('Длина превышает 100 символов')
        return title


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='повторите пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

