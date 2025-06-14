from django.shortcuts import render

from .models import Post, Categoria, Autor
from .forms import AutorForm, CategoriaForm, PostForm, BusquedaPostForm, BusquedaCategoriaForm, BusquedaAutorForm

def inicio(request):
    return render(request, 'PaginaBlog/index.html')

def crear_autor(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AutorForm()
    return render(request, 'PaginaBlog/formulario.html', {'form': form, 'titulo': 'Crear Autor'})

def crear_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CategoriaForm()
    return render(request, 'PaginaBlog/formulario.html', {'form': form, 'titulo': 'Crear Categoría'})

def crear_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PostForm()
    return render(request, 'PaginaBlog/formulario.html', {'form': form, 'titulo': 'Crear Post'})

def buscar_post(request):
    resultados = []
    if request.GET.get('titulo'):
        form = BusquedaPostForm(request.GET or None)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            resultados = Post.objects.filter(titulo__icontains=titulo)
    else:
        form = BusquedaPostForm()
        print("RESULTADOS:", resultados)
        for r in resultados:
            print("->", r.titulo)
    return render(request, 'PaginaBlog/buscar.html', {'form': form, 'resultados': resultados, 'tipo': 'post'})

def buscar_categoria(request):
    resultados = []
    form = BusquedaCategoriaForm(request.GET or None)
    if form.is_valid():
        nombre = form.cleaned_data['nombre']
        resultados = Categoria.objects.filter(nombre__icontains=nombre)
    print("Categorías encontradas:", resultados) 
    return render(request, 'PaginaBlog/buscar.html', {'form': form, 'resultados': resultados, 'tipo': 'categoria'})

def buscar_autor(request):
    resultados = []
    form = BusquedaAutorForm(request.GET or None)
    if form.is_valid():
        nombre = form.cleaned_data['nombre']
        resultados = Autor.objects.filter(nombre__icontains=nombre)
    print("Autores encontrados:", resultados) 
    return render(request, 'PaginaBlog/buscar.html', {'form': form, 'resultados': resultados, 'tipo': 'autor'})
