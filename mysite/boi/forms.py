from .models import UserProfile
from django.contrib.auth.models import User
from django import forms
from .models import Mercadoria


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')

class MercForm(forms.ModelForm):
    class Meta:
        model = Mercadoria
        fields = ('codigo','tipo_mercadoria','nome','quantidade','preco','tipo_negocio')
