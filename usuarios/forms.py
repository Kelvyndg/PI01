from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm


class UsuarioForm(UserCreationForm):
    email = forms.EmailField(max_length=100)







    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', ]
