from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Libros(models.Model):

    titulo=models.CharField(max_length=40)
    año=models.IntegerField()
    nombreautor=models.CharField(max_length=40)
    apellidoautor=models.CharField(max_length=40)
    genero=models.CharField(max_length=40)
    precio=models.IntegerField()

    def __str__(self):
        return f"Título: {self.titulo} - Año: {self.año} "


class Usuarios(models.Model):
    nombreusuario=models.CharField(max_length=40)
    apellidousuario=models.CharField(max_length=40)
    mail=models.CharField(max_length=40)
    edad=models.IntegerField()
    direccion=models.CharField(max_length=40)
    localidad=models.CharField(max_length=40)
    usuario=models.CharField(max_length=40)
    clave=models.IntegerField()

    def __str__(self):
        return f"{self.nombreusuario} {self.apellidousuario}, {self.edad} años, reside en {self.localidad}"

class Vinilos(models.Model):
    artista=models.CharField(max_length=40)
    añovinilo=models.IntegerField()
    nombrevinilo=models.CharField(max_length=40)
    preciovinilo=models.IntegerField()

    def __str__(self):
        return f"Título: {self.nombrevinilo} - Artista: {self.artista}"

class Avatar(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    imagen= models.ImageField(upload_to='avatares',null=True, blank=True)



class Mensajes(models.Model):

    usuariomensaje=models.CharField(max_length=40)
    comentario=models.CharField(max_length=2000 )

    def __str__(self):
        return f"Usuario: {self.usuariomensaje} - Mensaje: {self.comentario}"

