from django.contrib import admin

# Register your models here.

from .models import Livro, Pessoa, Capitulo

class LivroAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'autor', 'categoria')
    exclude = ['autor']

    def get_queryset(self, request):
        qs = super(LivroAdmin, self).get_queryset(request)
        return qs.filter(autor=request.user)
    
    def save_model(self, request, obj, form, change):
        obj.autor = request.user
        super().save_model(request, obj, form, change)
    

class CapituloAdmin(admin.ModelAdmin):
    list_display = ('id', 'numero', 'titulo', 'livro')


class PessoaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'tpUser')

admin.site.register(Livro, LivroAdmin)
admin.site.register(Capitulo, CapituloAdmin)
admin.site.register(Pessoa)