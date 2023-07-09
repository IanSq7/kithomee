
from django import forms
from .models import Producto


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)




class   ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'


