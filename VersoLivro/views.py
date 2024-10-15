from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
from django.contrib import messages
from .models import Livro, Capitulo
from .forms import LivroModelForm, CapModelForm, EditaLivroForm, EditaCapForm, CriaUserForm


def index(request):
    livros = Livro.objects.all()
    context = {
        'livros': livros
    }
    return render(request, 'index.html', context)


def registro(request):
    if request.method == 'POST':
        form = CriaUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirecione para a página de login após o registro
    else:
        form = CriaUserForm()
    return render(request, 'registro.html', {'form': form})



def livro (request, pk):
    livro = get_object_or_404(Livro, id=pk)
    capitulo = Capitulo.objects.filter(livro=livro)
    context = {
        'livro': livro,
        'capitulo': capitulo
    }
    return render(request, 'livro.html', context)


def livroForm(request):
    if (request.method) == 'POST':
        form = LivroModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Livro salvo com sucesso.')
            form = LivroModelForm()
        else:
            messages.error(request, 'Erro ao salvar livro.')
    else:
        form = LivroModelForm()

    context = {
        'form': form
    }
    return render(request, 'livroForm.html', context)

def editLivro(request, id=None):
    if id:
        livro = get_object_or_404(Livro, id=id)
        if ((livro.autor != request.user) and  (not request.user.groups.filter(name='Administrador').exists())):
            livros = Livro.objects.all()
            context = {
                'livros': livros
            }
            return render(request, 'index.html', context)        
    else:
        livro = Livro(autor=request.user)

    form = EditaLivroForm(request.POST or None, instance=livro)
    if (request.POST and form.is_valid()):
        form.save()
        messages.success(request, 'Livro editado com sucesso!')
        form = EditaLivroForm()
    
    context = {
        'form': form,
        'livro': livro
    }
    return render(request, 'editLivro.html', context)

def deletLivro(request, id=None):
    if id:
        livro = get_object_or_404(Livro, id=id)
        if ((livro.autor != request.user) and  (not request.user.groups.filter(name='Administrador').exists())):
            livros = Livro.objects.all()
            context = {
                'livros': livros
            }
            return render(request, 'index.html', context)        

    livro = Livro.objects.get(id = id)
    livro.delete()
    livros = Livro.objects.all()
    context = {
        'livros': livros
    }
    return render(request, 'index.html', context)

def verCapitulo(request, id):
    capitulo = Capitulo.objects.get(id = id)

    context = {
        'capitulo': capitulo
    }
    return render(request, 'verCapitulo.html', context)

def capForm(request, id):

    livro = get_object_or_404(Livro, id=id)
    if ((livro.autor != request.user) and  (not request.user.groups.filter(name='Administrador').exists())):
        livros = Livro.objects.all()
        context = {
            'livros': livros
        }
        return render(request, 'index.html', context)   
  
    if (request.method) == 'POST':
        form = CapModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Capitulo cadastrado com sucesso!')
            form = CapModelForm()
        else:
            messages.error(request, 'Erro ao cadastrar capitulo')
    else:
        form = CapModelForm()

    context = {
        'form' : form,
        'livro': livro,
    }
    return render(request, 'capForm.html', context)

def editCap(request, id):
    if id:
        capitulo = Capitulo.objects.get(id = id)
        if ((capitulo.livro.autor != request.user) and  (not request.user.groups.filter(name='Administrador').exists())):   
            livros = Livro.objects.all()
            context = {
                'livros': livros
            }
            return render(request, 'index.html', context)           
    else:
        capitulo = Capitulo.objects.get(id = id)

    form = EditaCapForm(request.POST or None, instance=capitulo)
    if (request.POST and form.is_valid()):
        form.save()
        messages.success(request, 'Capitulo editado com sucesso!')
        form = EditaCapForm()
    
    context = {
        'form': form,
        'capitulo': capitulo
    }
    return render(request, 'editCapitulo.html', context)

def deletCap(request, id=None):
    if id:
        capitulo = Capitulo.objects.get(id = id)   
        if ((capitulo.livro.autor != request.user) and  (not request.user.groups.filter(name='Administrador').exists())): 
            livros = Livro.objects.all()
            context = {
                'livros': livros
            }
            return render(request, 'index.html', context)

    capitulo = Capitulo.objects.get(id = id)     
    capitulo.delete()
    livros = Livro.objects.all()
    context = {
        'livros': livros
    }
    return render(request, 'index.html', context)

def login_View(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                livros = Livro.objects.all()
                context = {
                    'livros': livros
                }  
                return render(request, 'index.html', context)
                
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})


def logout_View(request):

    logout(request)
    messages.success(request, "Você saiu com sucesso.")
    livros = Livro.objects.all()
    context = {
            'livros': livros
    }  
    return render(request, 'index.html', context)

def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html: charset=utf8', status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html: charset=utf8', status=500)