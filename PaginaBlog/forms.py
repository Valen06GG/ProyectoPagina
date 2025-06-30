from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Autor, Categoria, Post, Avatar

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class BusquedaAutorForm(forms.Form):
    nombre = forms.CharField(label="Nombre del Autor", max_length=100, required=False)

class BusquedaCategoriaForm(forms.Form):
    nombre = forms.CharField(label="Nombre de la Categoría", max_length=100, required=False)

class BusquedaPostForm(forms.Form):
    titulo = forms.CharField(label="Título del Post", max_length=100, required=False)

class UserEditForm(UserCreationForm):
    class Meta:
        model = User
        fields = [ 'username', 'email', 'last_name', 'first_name' ]

    
    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        self.fields['username'].required = True

class AvatarFormulario(forms.Form):
    class Meta:
        model = Avatar
        
        fields = ['imagen']

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']
