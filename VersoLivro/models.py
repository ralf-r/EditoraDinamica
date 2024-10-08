from django.db import models
from django.contrib.auth import get_user_model
from django.core.files.storage import FileSystemStorage
#from stdimage.models import StdImageField

# Create your models here.

fs = FileSystemStorage(location="VersoLivro/static/img")
TIPO_CATEGORIA = {
    "A": "Autoajuda",
    "B": "Bibliografia",
    "C": "Comedia",
    "E": "Epico",
    "I": "Infantil",
    "L": "Literatura",
    "M": "Matematica",
    "P": "Poesia",
    "R": "Romance",
    "T": "Terror",
    }



class Livro(models.Model):
   
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, help_text='nome')
    autor = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)
    categoria = models.CharField(max_length=1, choices=TIPO_CATEGORIA, default='SELECIONE')
    capa = models.ImageField(storage=fs)
    sinopse = models.TextField(default='Sinopse..')

    def __str__(self):
        return f'{self.titulo} {self.categoria} {self.capa} {self.sinopse}'
    


class Pessoa(models.Model):
    TIPO_USUARIO = {
        "E": "EDITOR",
        "R": "REVISOR",
        "L": "LEITOR",
    } 

    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, help_text='nome')
    email = models.EmailField(help_text='Informe o email', max_length=70)
    tpUser = models.CharField(max_length=1, choices=TIPO_USUARIO)

    def __str__(self):
        return f'{self.id} {self.nome}'