from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Usuario, Venta,Region, Comuna, Direccion





class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label="nombre de usuario", min_length=4, max_length=150,required=True)
    email = forms.EmailField(label="correo electrónico",required=True)
    password1 = forms.CharField(label="contraseña", widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(
        label="confirma tu contraseña", widget=forms.PasswordInput,
        required=True
    )