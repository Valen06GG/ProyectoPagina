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
# requirements.txt

# Requisitos:
# Python 3.11 
# pip

# Clonar el repositorio:
# Yo lo hago desde la powershell pero dejo el proceso:
#     
#     git clone "carpetas correspondientes donde seencuentra el proyecto/ProyectoPagina"
#     cd /ProyectoPagina/
#     code.

# activar un entorno virtual:
# python -m venv .venv
# source .venv/bin/activate  # Para Windows: .venv\Scripts\activate

# Instalar dependencias:
# pip install -r requirements.txt

# Configuracion:
# Hacer la migracion:   python manage.py migrate
 
# Crear un superusuario:
# python manage.py createsuperuser

# Levantar el servidor:
# python manage.py runserver
# Proyecto disponible en http://127.0.0.1:8000/PaginaBlog/

# Para agregar nuevas apps:
# python manage.py startapp nombre_app

# Para entrar al panel de administración:
# http://127.0.0.1:8000/admin/