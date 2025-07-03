from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from .views import ( PostToggleEstadoView, AutorDetailView, CategoriaDetailView, PostDetailView,
    AutorDeleteView, PostDeleteView, CategoriaDeleteView,
    PostEditarView, AutorEditarView, CategoriaEditarView,
    PostsPorAutorView
)

urlpatterns = [

    #Busquedas y Creaciones
    path('', views.inicio, name="Inicio"),
    path('autor/', views.crear_autor, name="CrearAutor"),
    path('categoria/', views.crear_categoria, name="CrearCategoria"),
    path('post/', views.crear_post, name="CrearPost"),
    path('buscar_post/', views.buscar_post, name="BuscarPost"),
    path('buscar_autor/', views.buscar_autor, name="BuscarAutor"),
    path('buscar_cat/', views.buscar_categoria, name="BuscarCategoria"),

    #Accesos del usuario
    path('perfil/', views.Perfil, name='Perfil'),
    path('editarPerfil/', views.editarPerfil, name='EditarPerfil'), 
    path('upload_avatar/', views.upload_avatar, name='upload_avatar'), 
    path('login/', views.login_request, name="Login"),
    path('logout/', LogoutView.as_view(next_page='Inicio'), name='Logout'),
    path('register/', views.registro, name='Register'),
    path('about me/', views.About, name='About'),
    path('editar-avatar/', views.editar_avatar, name='editarAvatar'),
  

    #Autor
    path('autor/<int:pk>/eliminar/', AutorDeleteView.as_view(), name='autor_delete'),
    path('autor/<int:pk>/', AutorDetailView.as_view(), name='autor_detail'),
    path('autor/<int:pk>/editar/', AutorEditarView.as_view(), name='autor_editar'),

    #Post
    path('post/<int:post_id>/estado/', PostToggleEstadoView.as_view(), name='post_toggle_estado'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/eliminar/', PostDeleteView.as_view(), name='post_delete'),
    path('autor/<int:autor_id>/posts/', PostsPorAutorView.as_view(), name='posts_por_autor'),
    path('post/<int:pk>/editar/', PostEditarView.as_view(), name='post_editar'),

    #Categorias
    path('categoria/<int:pk>/eliminar/', CategoriaDeleteView.as_view(), name='categoria_delete'),
    path('categoria/<int:pk>/', CategoriaDetailView.as_view(), name='categoria_detail'),
    path('categoria/<int:pk>/editar/', CategoriaEditarView.as_view(), name='categoria_editar'),
]
