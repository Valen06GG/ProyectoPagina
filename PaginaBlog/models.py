from django.db import models
from django.contrib.auth.models import User

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre
    
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha = models.DateField(auto_now_add=True)
    autor = models.ForeignKey('Autor', on_delete=models.CASCADE)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)

    estados = [
        ('Publicado', 'Publicado'),
        ('Borrador', 'Borrador'),
    ]
    estado = models.CharField(max_length=10, choices=estados, default='Borrador')

    def __str__(self):
        return self.titulo

class Avatar(models.Model):
   
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatar', null=True, blank = True)
    birthdate = models.DateField(null=True, blank=True)
    

    def __str__(self):
        return f"{self.user} - {self.imagen}" 

