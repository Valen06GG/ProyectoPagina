from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import login, logout, authenticate
from .models import Post, Categoria, Autor, Avatar
from .forms import AutorForm, CategoriaForm, PostForm, BusquedaPostForm, BusquedaCategoriaForm, BusquedaAutorForm, UserEditForm, AvatarForm, UserRegisterForm
from django.urls import reverse

@login_required
def inicio(request):

        avatar = Avatar.objects.filter(user=request.user.id)

        return render(request, 'PaginaBlog/index.html')

def crear_autor(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Inicio')
    else:
        form = AutorForm()
    return render(request, 'PaginaBlog/formulario.html', {'form': form, 'titulo': 'Crear Autor'})

def crear_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Inicio')
    else:
        form = CategoriaForm()
    return render(request, 'PaginaBlog/formulario.html', {'form': form, 'titulo': 'Crear Categoría'})

def crear_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Inicio')
    else:
        form = PostForm()
    return render(request, 'PaginaBlog/formulario.html', {'form': form, 'titulo': 'Crear Post'})

def buscar_post(request):
    form = BusquedaPostForm(request.GET or None)

    resultados = Post.objects.all()  # por defecto, mostrar todos

    if request.method == 'GET':
        if form.is_valid():
            titulo = form.cleaned_data.get('titulo', '')
            if titulo:  # si escribió algo
                resultados = Post.objects.filter(titulo__icontains=titulo)

    return render(request, 'PaginaBlog/buscar.html', {
        'form': form,
        'resultados': resultados,
        'tipo': 'post'
    })

def buscar_categoria(request):
    resultados = []
    form = BusquedaCategoriaForm(request.GET or None)
    if form.is_valid():
        nombre = form.cleaned_data['nombre']
        resultados = Categoria.objects.filter(nombre__icontains=nombre)
        print("Categorías encontradas:", resultados) 
    else:
        resultados = Categoria.objects.all()
    return render(request, 'PaginaBlog/buscar.html', {
        'form': form,
        'resultados': resultados,
        'tipo': 'categoria'
    })

def buscar_autor(request):
    resultados = []
    form = BusquedaAutorForm(request.GET or None)
    if form.is_valid():
        nombre = form.cleaned_data['nombre']
        resultados = Autor.objects.filter(nombre__icontains=nombre)
        print("Autores encontrados:", resultados)
    else:
        resultados = Autor.objects.all()
    return render(request, 'PaginaBlog/buscar.html', {
        'form': form,
        'resultados': resultados,
        'tipo': 'autor'
    })
    
    
def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password= password)

            if user is not None:
                login(request, user)

                return redirect('Inicio')
        
        else:
                messages.error(request, "Usuario o Contraseña invalidos")

    form = AuthenticationForm()
    return render(request, 'PaginaBlog/login.html', {'form':form} )

@login_required
def editarPerfil(request):
    usuario = request.user

    if request.method == "POST":
        mi_formulario = UserEditForm(request.POST, instance=usuario)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data

            if informacion.get('password1', '') != '':
                if informacion['password1'] == informacion.get('password2', ''):
                    usuario.set_password(informacion['password1'])
                else:
                    mi_formulario.add_error('password2', 'Las contraseñas no coinciden')
                    return render(request, "PaginaBlog/editarPerfil.html", {"formulario": mi_formulario})

            mi_formulario.save()
            return redirect('Inicio')
    else:
        mi_formulario = UserEditForm(instance=usuario)

    return render(request, "PaginaBlog/editarPerfil.html", {"formulario": mi_formulario})

def registro(request):

      if request.method == 'POST':

            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"PaginaBlog/index.html" ,  {"mensaje":"Usuario Creado :)"})

      else:                  
            form = UserRegisterForm()     

      return render(request,"PaginaBlog/registro.html" ,  {"form":form})

@login_required
def upload_avatar(request):
    avatar = Avatar.objects.filter(user=request.user.id).first()
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES, instance=avatar)
        if form.is_valid():
            avatar = form.save(commit=False)
            avatar.user = request.user
            form.save()
            return redirect('Inicio')
    else:
        form = AvatarForm(instance=avatar)
    return render(request, 'PaginaBlog/upload_avatar.html', {'form': form})

@login_required
def post_toggle_estado(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        nuevo_estado = request.POST.get('estado')
        if nuevo_estado in ['publicado', 'borrador']:
            post.estado = nuevo_estado
            post.save()
            return redirect('BuscarPost')  

    return render(request, 'PaginaBlog/post_toggle_estado.html', {'post': post})

def autor_detail(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    return render(request, 'PaginaBlog/autor_detail.html', {'autor': autor})

def autor_delete(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    autor.delete()
    return redirect('BuscarAutor')

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('BuscarPost')

def categoria_delete(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    categoria.delete()
    return redirect('BuscarCategoria')

def categoria_detail(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    return render(request, 'PaginaBlog/categoria_detail.html', {'categoria': categoria})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'PaginaBlog/post_detail.html', {'post': post})