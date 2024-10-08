from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
# Create your views here.
from .models import Livro
from .forms import LivroForm

def index(request):
    livros = Livro.objects.all()
    context = {
        'livros': livros
    }
    return render(request, 'index.html', context)



def livro (request, pk):
    liv = get_object_or_404(Livro, id=pk)
    context = {
        'livro': liv
    }
    return render(request, 'livro.html', context)


def livroForm(request):
    form = LivroForm(request.POST, request.FILES)
    context = {}

    if request.method == 'POST':
        if form.is_valid():
            id = form.cleaned_data['id']
            titulo = form.cleaned_data['titulo']
            autor = form.cleaned_data['autor']
            categoria = form.cleaned_data['categoria']
            capa = form.cleaned_data['capa']
            sinopse = form.cleaned_data['sinopse']

            obj = Livro.objects.create(
                id = id, 
                titulo = titulo,
                autor = autor,
                categoria = categoria,
                capa = capa,
                sinopse = sinopse,
            )

            obj.save()
            print(obj)

            messages.success(request, 'Livro cadastrado com sucesso!')
            form = LivroForm()
        else:
            initial = {'name':request.user.username}
            messages.error(request, 'Erro ao cadastrar livro')

    context['form'] = form

    return render(request, 'livroForm.html', context)



def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html: charset=utf8', status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html: charset=utf8', status=500)