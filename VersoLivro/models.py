from django.db import models
from django.contrib.auth import get_user_model
from django.core.files.storage import FileSystemStorage
#from django.contrib.auth.models import AbstractUser, BaseUserManager

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
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)
    categoria = models.CharField(max_length=1, choices=TIPO_CATEGORIA, default='SELECIONE')
    capa = models.ImageField(storage=fs)
    sinopse = models.TextField(default='Sinopse..',max_length=200 )

    def __str__(self):
        return self.titulo
    


class Capitulo(models.Model):
    id = models.AutoField(primary_key=True)
    numero = models.IntegerField()
    titulo = models.CharField(max_length=30)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE,)
    texto = models.TextField(default='Texto..', max_length=500)

    def __str__(self):
        return f'{self.numero} {self.titulo}'



class Pessoa(models.Model):
    TIPO_USUARIO = {
        "E": "EDITOR",
        "R": "REVISOR",
        "L": "LEITOR",
    } 

    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, help_text='nome')
    email = models.EmailField('email', unique=True)
    tpUser = models.CharField(max_length=1, choices=TIPO_USUARIO)

    #USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = ['fist_nome', 'tpUser']

    def __str__(self):
        return self.email
    
    #objects = UserManager()