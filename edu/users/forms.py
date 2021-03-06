from django import forms
from .models import User

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from captcha import widgets, fields


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя аккаунта', max_length=18,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}))

    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    captcha = fields.ReCaptchaField(label='Капча', widget=widgets.ReCaptchaV2Checkbox())

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя аккаунта', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    captcha = fields.ReCaptchaField(label='Капча', widget=widgets.ReCaptchaV2Checkbox())

    class Meta:
        model = User
        fields = ('username', 'password')