from django.urls import path

from .views import index, livro, livroForm, capForm, editLivro, deletLivro, editCap, verCapitulo, deletCap

urlpatterns = [
    path('', index, name='index'),
    path('livro/<int:pk>', livro, name='livro'),
    path('livroForm/', livroForm, name='livroForm'),
    path('capForm/', capForm, name='capForm'),
    path('editaLivro/<int:id>', editLivro, name='editLivro'),
    path('capitulo/<int:id>', verCapitulo, name='verCapitulo'),
    path('deletLivro/<int:id>', deletLivro, name='deletLivro'),
    path('editCapitulo/<int:id>', editCap, name='editCap'),
    path('deletCapitulo/<int:id>', deletCap, name='deletCap'),
]