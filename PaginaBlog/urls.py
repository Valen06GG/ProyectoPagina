from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('autor/', views.crear_autor, name="CrearAutor"),
    path('categoria/', views.crear_categoria, name="CrearCategoria"),
    path('post/', views.crear_post, name="CrearPost"),
    path('buscar/', views.buscar_post, name="BuscarPost"),
    path('buscar_post/', views.buscar_post, name="BuscarPost"),
    path('buscar_autor/', views.buscar_autor, name="BuscarAutor"),
    path('buscar_cat/', views.buscar_categoria, name="BuscarCategoria"),
    path('editarPerfil/', views.editarPerfil, name='EditarPerfil'), 
    path('agregarAvatar/', views.agregarAvatar, name='AgregarAvatar'), 
    path('login/', views.login_request, name="Login"),
    path('logout/', LogoutView.as_view(next_page='Inicio'), name='Logout'),
    path('register/', views.registro, name='Register'),
]
