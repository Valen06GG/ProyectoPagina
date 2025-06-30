from django.contrib import admin
from .models import Autor, Categoria, Post, Avatar

admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(Post)
admin.site.register(Avatar)
