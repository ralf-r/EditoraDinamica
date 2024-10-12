from django import forms
from .models import TIPO_CATEGORIA, Livro, Capitulo
from rest_framework import serializers

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