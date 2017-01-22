from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="", help_text="", max_length=30,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'name': 'username', 'placeholder': 'Username'}))
    password = forms.CharField(label="", help_text="", max_length=30,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'name': 'password', 'type': 'password',
                                          'placeholder': 'Password'}))
