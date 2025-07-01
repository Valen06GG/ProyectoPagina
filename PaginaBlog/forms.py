from typing import Any
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
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

class UserEditForm(UserChangeForm):
    password = None

    password = forms.CharField(label="password", widget=forms.PasswordInput, required=False)
    password_confirm = forms.CharField(label="password confirm", widget=forms.PasswordInput, required=False)


    class Meta:
        model = User
        fields = [ 'username', 'email', 'last_name', 'first_name' ]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password or password_confirm:
            if password != password_confirm:
                raise forms.ValidationError("Las contraseñas no coinciden.")
            if password and len(password) < 8:
                raise forms.ValidationError("La contraseña debe tener al menos 8 caracteres.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('inicio')  # Login exitoso
            else:
                messages.error(request, 'Usuario o contraseña incorrectos')
    else:
        form = LoginForm()

    return render(request, 'PaginaBlog/login.html', {'form': form})

class AvatarForm(forms.ModelForm):


    class Meta:
        model = Avatar
        fields = ['imagen']


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)