from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Libros_formulario(forms.Form):
    titulo=forms.CharField(max_length=40)
    año=forms.IntegerField()
    nombreautor=forms.CharField(max_length=40)
    apellidoautor=forms.CharField(max_length=40)
    genero=forms.CharField(max_length=40)
    precio=forms.IntegerField()

class Vinilos_formulario(forms.Form):
    artista=forms.CharField(max_length=40)
    añovinilo=forms.IntegerField()
    nombrevinilo=forms.CharField(max_length=40)
    preciovinilo=forms.IntegerField()

class Usuarios_formulario(forms.Form):
    nombreusuario=forms.CharField(max_length=40)
    apellidousuario=forms.CharField(max_length=40)
    mail=forms.CharField(max_length=40)
    edad=forms.IntegerField()
    direccion=forms.CharField(max_length=40)
    localidad=forms.CharField(max_length=40)
    usuario=forms.CharField(max_length=40)
    clave=forms.IntegerField()

class UserEditForm (UserCreationForm):
    
    email=forms.EmailField(label="Modificar")
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields= ['email','password1','password2']       
        help_text= {k:"" for k in fields}


class Mensajes_formulario(forms.Form):
    usuariomensaje=forms.CharField(max_length=40)
    comentario=forms.CharField(max_length=2000)