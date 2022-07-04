import django
from django.urls import path
from django import views
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns= [

path("",views.inicio,name="Inicio"),
path("libros",views.libros, name="libros"),
path("usuarios",views.usuarios, name="usuarios"),
path("vinilos",views.vinilos, name="vinilos"),
path("alta_libros", views.libros_formulario,name="alta_libros"),
path("buscar_libros",views.buscar_libros,name="buscar_libros"),
path("buscar",views.buscar),
path("alta_vinilos", views.vinilos_formulario,name="alta_vinilos"),
path("buscar_vinilos",views.buscar_vinilos,name="buscar_vinilos"),
path("buscarvinilos",views.buscarvinilos),
path("alta_usuarios", views.usuarios_formulario,name="alta_usuarios"),
path("eliminalibros/<int:id>", views.eliminalibros, name="eliminalibros"),
path("eliminavinilos/<int:id>", views.eliminavinilos, name="eliminavinilos"),
path("editarlibros/<int:id>", views.editarlibros,name="editarlibros"),
path("editarlibros/", views.editarlibros, name="editarlibros"),
path("editarvinilos/<int:id>", views.editarvinilos,name="editarvinilos"),
path("editarvinilos/", views.editarvinilos, name="editarvinilos"),
path("login",views.login_request, name="Login"),
path("register",views.register, name="Register"),
path("logout",LogoutView.as_view(template_name="logout.html"),name="Logout"),
path("editarPerfil", views.editarPerfil, name="editarPerfil"),
path("mensajes", views.mensajes_formulario,name="mensajes"),
path("eliminamensajes/<int:id>", views.eliminamensajes, name="eliminamensajes"),
path("editarmensajes/<int:id>", views.editarmensajes,name="editarmensajes"),
path("editarmensajes/", views.editarmensajes, name="editarmensajes"),
path("listamensajes",views.listamensajes, name="listamensajes"),
path("eliminamensajes/mensajes",views.mensajes_formulario, name="mensajes"),
path("editarmensajes/mensajes",views.mensajes_formulario, name="mensajes"),
path("eliminalibros/alta_libros",views.libros_formulario, name="alta_libros"),
path("editarlibros/alta_libros",views.libros_formulario, name="alta_libros"),
path("eliminavinilos/alta_vinilos",views.vinilos_formulario, name="alta_vinilos"),
path("editarvinilos/alta_vinilos",views.vinilos_formulario, name="alta_vinilos"),
path("aboutme",views.aboutme, name="aboutme"),
path("pages",views.pages, name="pages"),
path("pages/readmore",views.readmore, name="readmore"),
path("video",views.video, name="video")







]