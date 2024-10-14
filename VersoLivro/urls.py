from django.urls import path
from django.contrib.auth import views as auth_views

from .views import index, livro, livroForm, capForm, editLivro, deletLivro, editCap, verCapitulo, deletCap, registro, login_View, logout_View

urlpatterns = [
    path('', index, name='index'),
    path('livro/<int:pk>', livro, name='livro'),
    path('livroForm/', livroForm, name='livroForm'),
    path('capForm/<int:id>', capForm, name='capForm'),
    path('editaLivro/<int:id>', editLivro, name='editLivro'),
    path('capitulo/<int:id>', verCapitulo, name='verCapitulo'),
    path('deletLivro/<int:id>', deletLivro, name='deletLivro'),
    path('editCapitulo/<int:id>', editCap, name='editCap'),
    path('deletCapitulo/<int:id>', deletCap, name='deletCap'),
    path('registro/', registro, name='registro'),
    path('login/', login_View, name='login'),
    path('logout/', logout_View, name='logout'),
]