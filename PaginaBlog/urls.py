from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('autor/', views.crear_autor, name="CrearAutor"),
    path('categoria/', views.crear_categoria, name="CrearCategoria"),
    path('post/', views.crear_post, name="CrearPost"),
    path('buscar_post/', views.buscar_post, name="BuscarPost"),
    path('buscar_autor/', views.buscar_autor, name="BuscarAutor"),
    path('buscar_cat/', views.buscar_categoria, name="BuscarCategoria"),
    path('editarPerfil/', views.editarPerfil, name='EditarPerfil'), 
    path('upload_avatar/', views.upload_avatar, name='upload_avatar'), 
    path('login/', views.login_request, name="Login"),
    path('logout/', LogoutView.as_view(next_page='Inicio'), name='Logout'),
    path('register/', views.registro, name='Register'),
    path('autor/<int:pk>/eliminar/', views.autor_delete, name='autor_delete'),
    path('autor/<int:pk>/', views.autor_detail, name='autor_detail'),
    path('post/<int:post_id>/cambiar_estado/', views.post_toggle_estado, name='post_toggle_estado'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/eliminar/', views.post_delete, name='post_delete'),
    path('categoria/<int:pk>/eliminar/', views.categoria_delete, name='categoria_delete'),
    path('categoria/<int:pk>/', views.categoria_detail, name='categoria_detail'),
]
