from django.urls import path

from .views import index, livro, livroForm

urlpatterns = [
    path('', index, name='index'),
    path('livro/<int:pk>', livro, name='livro'),
    path('livroForm', livroForm, name='livroForm'),
]