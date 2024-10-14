from django import forms
from .models import TIPO_CATEGORIA, Livro, Capitulo
from rest_framework import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LivroModelForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'categoria', 'capa','sinopse']


class CapModelForm(forms.ModelForm):
     class Meta:
        model = Capitulo
        fields = ['numero', 'titulo', 'livro', 'texto']


class EditaLivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = '__all__'


class EditaCapForm(forms.ModelForm):
    class Meta:
        model = Capitulo
        fields = '__all__'


class CriaUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'groups', 'first_name', 'last_name')