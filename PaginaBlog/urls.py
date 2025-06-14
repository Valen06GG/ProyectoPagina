from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('autor/', views.crear_autor, name="CrearAutor"),
    path('categoria/', views.crear_categoria, name="CrearCategoria"),
    path('post/', views.crear_post, name="CrearPost"),
    path('buscar/', views.buscar_post, name="BuscarPost"),
    path('buscar_post/', views.buscar_post, name="BuscarPost"),
    path('buscar_autor/', views.buscar_autor, name="BuscarAutor"),
    path('buscar_cat/', views.buscar_categoria, name="BuscarCategoria"),
]
