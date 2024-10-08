from django import forms
from .models import TIPO_CATEGORIA
from rest_framework import serializers

class LivroForm(forms.Form):
    id = forms.IntegerField(required=False, widget=forms.HiddenInput())
    titulo = forms.CharField(label='Titulo', max_length=100)
    autor = serializers.CharField(source='autor', read_only=True)
    categoria = forms.ChoiceField(choices=TIPO_CATEGORIA)
    capa = forms.ImageField()
    sinopse = forms.CharField(label='Sinopse', widget=forms.Textarea(), max_length=500)