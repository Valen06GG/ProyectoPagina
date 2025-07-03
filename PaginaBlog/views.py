from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import login, logout, authenticate
from .models import Post, Categoria, Autor, Avatar
from .forms import AutorForm, CategoriaForm, PostForm, BusquedaPostForm, BusquedaCategoriaForm, BusquedaAutorForm, UserEditForm, AvatarForm, UserRegisterForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic import ListView


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
        form = AuthenticationForm()

    return render(request, 'PaginaBlog/login.html', {'form':form} )

@login_required
def editarPerfil(request):
    usuario = request.user
    avatar = Avatar.objects.filter(user=usuario).first()

    if request.method == "POST":
        mi_formulario = UserEditForm(request.POST, instance=usuario)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data

            if informacion.get('password1', '') != '':
                if informacion['password1'] == informacion.get('password2', ''):
                    usuario.set_password(informacion['password1'])
                else:
                    mi_formulario.add_error('password2', 'Las contraseñas no coinciden')
                    return render(request, "PaginaBlog/editarPerfil.html", {
                        "formulario": mi_formulario,
                        "avatar": avatar  
                    })

            mi_formulario.save()
            return redirect('Inicio')
    else:
        mi_formulario = UserEditForm(instance=usuario)

    return render(request, "PaginaBlog/editarPerfil.html", {
        "formulario": mi_formulario,
        "avatar": avatar  
    })

def registro(request):

      if request.method == 'POST':

            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"PaginaBlog/index.html")

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


class PostToggleEstadoView(LoginRequiredMixin, View):
    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        return render(request, 'PaginaBlog/post_estado.html', {'post': post})

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        nuevo_estado = request.POST.get('estado')
        if nuevo_estado in ['publicado', 'borrador']:
            post.estado = nuevo_estado
            post.save()
        return redirect('BuscarPost')
    
class AutorDetailView(DetailView):
    model = Autor
    template_name = 'PaginaBlog/autor_detail.html'
    context_object_name = 'autor'

class CategoriaDetailView(DetailView):
    model = Categoria
    template_name = 'PaginaBlog/categoria_detail.html'
    context_object_name = 'categoria'

class PostDetailView(DetailView):
    model = Post
    template_name = 'PaginaBlog/post_detail.html'
    context_object_name = 'post'

class AutorDeleteView(LoginRequiredMixin, DeleteView):
    model = Autor
    success_url = reverse_lazy('BuscarAutor')

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('BuscarPost')

class CategoriaDeleteView(LoginRequiredMixin, DeleteView):
    model = Categoria
    success_url = reverse_lazy('BuscarCategoria')

class PostEditarView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'PaginaBlog/editar_post.html'
    success_url = reverse_lazy('BuscarPost')

class AutorEditarView(LoginRequiredMixin, UpdateView):
    model = Autor
    form_class = AutorForm
    template_name = 'PaginaBlog/editar_autor.html'
    success_url = reverse_lazy('BuscarAutor')

class CategoriaEditarView(LoginRequiredMixin, UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'PaginaBlog/editar_categoria.html'
    success_url = reverse_lazy('BuscarCategoria')

class PostsPorAutorView(ListView):
    model = Post
    template_name = 'PaginaBlog/posts_por_autor.html'
    context_object_name = 'posts'

    def get_queryset(self):
        self.autor = get_object_or_404(Autor, id=self.kwargs['autor_id'])
        return Post.objects.filter(autor=self.autor)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['autor'] = self.autor
        return context
    
def About(request):
    return render(request, 'PaginaBlog/About_me.html')
        
def Perfil(request):
    avatar = Avatar.objects.filter(user=request.user).first()
    return render(request, 'PaginaBlog/Perfil.html', {
        'usuario': request.user,
        'avatar': avatar
    })
@login_required
def editar_avatar(request):
    avatar = Avatar.objects.filter(user=request.user).first()
    
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES, instance=avatar)
        if form.is_valid():
            form.save()
            messages.success(request, 'Avatar actualizado correctamente.')
            return redirect('editarPerfil')  # Redirige después de guardar el avatar
    else:
        form = AvatarForm(instance=avatar)

    return render(request, 'PaginaBlog/editar_avatar.html', {'form': form, 'avatar': avatar})
