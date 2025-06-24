from django.shortcuts import render, redirect
from .forms import AutorForm, CategoriaForm, PostForm, BuscarPostForm
from .models import Post

def crear_autor(request):
    form = AutorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('crear_post')
    return render(request, 'crear_autor.html', {'form': form})

def crear_categoria(request):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('crear_post')
    return render(request, 'crear_categoria.html', {'form': form})

def crear_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('crear_post')
    return render(request, 'crear_post.html', {'form': form})

def buscar_post(request):
    resultados = []
    form = BuscarPostForm(request.GET or None)
    if form.is_valid():
        titulo = form.cleaned_data.get('titulo')
        resultados = Post.objects.filter(titulo__icontains=titulo)
    return render(request, 'buscar_post.html', {'form': form, 'resultados': resultados})
def home(request):
    return render(request, 'home.html')
