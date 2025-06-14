from django import forms
from .models import Autor, Categoria, Post

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
    nombre = forms.CharField(label="Nombre del Autor", max_length=100)

class BusquedaCategoriaForm(forms.Form):
    nombre = forms.CharField(label="Nombre de la Categoría", max_length=100)

class BusquedaPostForm(forms.Form):
    titulo = forms.CharField(label="Título del Post", max_length=100)
