
from django import forms
from .models import Producto
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)




class   ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'


class CustomUserCreationForm(UserCreationForm):
    pass