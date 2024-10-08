from django.contrib import admin

# Register your models here.

from .models import Livro, Pessoa

class LivroAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'autor', 'categoria')


class PessoaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'tpUser')

admin.site.register(Livro, LivroAdmin)
admin.site.register(Pessoa)