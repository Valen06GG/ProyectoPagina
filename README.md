# ProyectoPagina

# Este proyecto es una aplicación web construida con Django, que permite a los usuarios registrarse, iniciar sesión, editar su perfil, gestionar su avatar, y visualizar publicaciones en un blog.

# Autenticación de Usuarios:
# Registro de nuevos usuarios.
# Inicio de sesión con validación de credenciales.
# Cierre de sesión desde cualquier parte del sitio.

# Perfil de Usuario
# Cada usuario tiene una sección personalizada donde puede ver:
# Su nombre, apellido y email.
# Su avatar.
# Su fecha de cumpleaños.
# Botón para editar su perfil directamente.

# Edición de Perfil
# Cambiar:
# Nombre de usuario.
# Email.
# Nombre y apellido.
# Contraseña (con confirmación).
# Fecha de cumpleaños.
# Botón para:
# Crear avatar si no tiene.
# Editar avatar si ya tiene uno.

# Gestión de Avatar
# Los usuarios pueden:
# Subir una imagen como avatar.
# Editar su imagen actual.
# Vista amigable para actualizar o cambiar el avatar.

# Blog
# Página principal tipo blog (por implementar o extender).
# Lugar para mostrar publicaciones o contenido público.

# PaginaBlog/
# ├── migrations
# ├── templates/
# │   ├── PaginaBlog/
# │   │   ├── index.html
# │   │   ├── login.html
# │   │   ├── editarPerfil.html
# │   │   ├── Perfil.html
# │   │   ├── About_me.html
# │   │   ├── autor_detail.html
# │   │   ├── buscar.html
# │   │   ├── categoria_detail.html
# │   │   ├── editar_autor.html
# │   │   ├── editar_categoria.html
# │   │   ├── editar_post.html
# │   │   ├── editarPerfil.html
# │   │   ├── formulario.html
# │   │   ├── post_detail.html
# │   │   ├── post_estado.html
# │   │   ├── posts_por_autor.html
# │   │   ├── registro.html
# │   │   └── upload_avatar.html
# ├── static/
# │   └── ... (CSS, JS, imágenes, etc.)
# ├── forms.py
# ├── models.py
# ├── views.py
# ├── urls.py
# ├── models.py
# ├── admin.py
# ├── apps.py
# ├── __init__.py
# ├── context_processors.py
# └── tests.py

# Proyecto
# ├── __pycache__
# ├── __init__.py
# ├── asgi.py
# ├── settings.py
# ├── urls.py
# ├── wsgi.py
# manage.py