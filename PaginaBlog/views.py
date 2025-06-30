from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import login, logout, authenticate
from .models import Post, Categoria, Autor, Avatar
from .forms import AutorForm, CategoriaForm, PostForm, BusquedaPostForm, BusquedaCategoriaForm, BusquedaAutorForm, UserEditForm, AvatarFormulario, AvatarForm
from django.urls import reverse

@login_required
def inicio(request):

        avatares = Avatar.objects.filter(user=request.user.id)

        if avatares.exists():
            url = avatares[0].imagen.url

        else:
            url = None 
  
        return render(request, 'PaginaBlog/index.html', {"url": url})

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

                return render(request, 'PaginaBlog/index.html', {"mensaje":f"Bienvenido {usuario}"} )
        
            else:
                return render(request, 'PaginaBlog/index.html', {"mensaje":"Error datos incorrectos"} )
        
        else:
                return render(request, 'PaginaBlog/index.html', {"mensaje":"Error, formulario erroneo"} )

    form = AuthenticationForm()
    return render(request, 'PaginaBlog/login.html', {'form':form} )

@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password1']
            usuario.save()
            return redirect('Inicio')

    else:
        miFormulario= UserEditForm(initial={ 'email':usuario.email})


    return render(request, 'PaginaBlog/editarPerfil.html', {'miFormulario':miFormulario, 'usuario':usuario}) 


@login_required
def agregarAvatar(request):
    
    miFornulario = AvatarFormulario(request.POST, request.FILES)

    if miFornulario.is_valid():

        u = User.objects.get(username=request.user)

        avatar = Avatar (user=u, imagen=miFornulario.cleaned_data)

        avatar.save()

        return render(request, "PaginaBlog/index.html")
    
    else:

        miFornulario= AvatarFormulario()
        avatar = Avatar.objects.filter(user=request.user).first()
    return render(request, 'PaginaBlog/agregarAvatar.html', {'avatar': avatar})

@login_required
def upload_avatar(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES, instance=request.user.avatar)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = AvatarForm(instance=request.user.avatar)
    return render(request, 'upload_avatar.html', {'form': form})

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Login')  # Redirige al login después de registrar
    else:
        form = UserCreationForm()
    return render(request, 'PaginaBlog/registro.html', {'form': form})
