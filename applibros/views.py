from django.shortcuts import render
from unittest import loader
from applibros.models import Libros, Usuarios, Vinilos, Avatar, Mensajes
from django.http import HttpResponse
from django.template import loader
from applibros.forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.template import RequestContext




# Create your views here.


def inicio (request):
    return render (request, "padre.html")

def aboutme (request):
    return render (request, "aboutme.html")

def pages (request):
    return render (request, "pages.html")

def readmore (request):
    return render (request, "readmore.html")

def video (request):
    return render (request, "video.html")


def usuarios (request):

    return render (request, "usuarios.html") 

@login_required
def libros(request):
    libros=Libros.objects.all()
    dicc={"libros":libros}
    plantilla=loader.get_template("libros.html")
    documento=plantilla.render(dicc)
    return HttpResponse(documento)

    return HttpResponse(libros)

def libros_formulario(request):
    if request.method=="POST":

        mi_formulario=Libros_formulario(request.POST)

        if mi_formulario. is_valid():
            datos=mi_formulario.cleaned_data

            
            libros=Libros(titulo=datos['titulo'], año=datos['año'], nombreautor=datos['nombreautor'], apellidoautor=datos['apellidoautor'], genero=datos['genero'], precio=datos['precio'])
            libros.save()
            

            return render (request, "formulario.html")


    return render (request, "formulario.html") 


def buscar_libros(request):
    
    return render(request, "buscar_libros.html")    


def buscar(request):
    if request.GET['titulo']:
        titulo=request.GET['titulo']
        libros=Libros.objects.filter(titulo__icontains=titulo)
        return render (request,"resultado_busqueda.html", {"libros":libros})
    else:
        return HttpResponse("Campo vacío")




def vinilos(request):
    vinilos=Vinilos.objects.all()
    dicc={"vinilos":vinilos}
    plantilla=loader.get_template("vinilos.html")
    documento=plantilla.render(dicc)
    return HttpResponse(documento)

    return HttpResponse(vinilos)

def vinilos_formulario(request):
    if request.method=="POST":

        mi_formulario=Vinilos_formulario(request.POST)

        if mi_formulario. is_valid():
            datos=mi_formulario.cleaned_data

            
            vinilos=Vinilos(artista=datos['artista'], añovinilo=datos['añovinilo'], nombrevinilo=datos['nombrevinilo'], preciovinilo=datos['preciovinilo'])
            vinilos.save()
            

            return render (request, "formulariovinilos.html")


    return render (request, "formulariovinilos.html") 


def buscar_vinilos(request):
    
    return render(request, "buscar_vinilos.html")    


def buscarvinilos (request):
    if request.GET['artista']:
        artista=request.GET['artista']
        vinilos=Vinilos.objects.filter(artista__icontains=artista)
        return render (request,"resultado_busquedavinilos.html", {"vinilos":vinilos})
    else:
        return HttpResponse("Campo vacío")



def usuarios(request):
    usuarios=Usuarios.objects.all()
    dicc={"usuarios":usuarios}
    plantilla=loader.get_template("usuarios.html")
    documento=plantilla.render(dicc)
    return HttpResponse(documento)

    return HttpResponse(usuarios)

def usuarios_formulario(request):
    if request.method=="POST":

        mi_formulario=Usuarios_formulario(request.POST)

        if mi_formulario. is_valid():
            datos=mi_formulario.cleaned_data

            
            usuarios=Usuarios(nombreusuario=datos['nombreusuario'], apellidousuario=datos['apellidousuario'], mail=datos['mail'], edad=datos['edad'], direccion=datos['direccion'], localidad=datos['localidad'], usuario=datos['usuario'], clave=datos['clave'])
            usuarios.save()
            

            return render (request, "formulariousuarios.html")


    return render (request, "formulariousuarios.html") 


def eliminalibros (request,id):

    libros=Libros.objects.get(id=id)
    libros.delete()

    libros=Libros.objects.all()

    return render(request,"libros.html", {"libros":libros})

def eliminavinilos (request,id):

    vinilos=Vinilos.objects.get(id=id)
    vinilos.delete()

    vinilos=Vinilos.objects.all()

    return render(request,"vinilos.html", {"vinilos":vinilos})

def editarlibros (request,id):
    libros=Libros.objects.get (id=id)
    if request.method=="POST":
        mi_formulario=Libros_formulario(request.POST)
        if mi_formulario.is_valid():
            datos=mi_formulario.cleaned_data
            libros.titulo=datos['titulo']
            libros.año=datos['año']
            libros.nombreautor=datos['nombreautor']
            libros.apellidoautor=datos['apellidoautor']
            libros.genero=datos['genero']
            libros.precio=datos['precio']
            libros.save()

            libros=Libros.objects.all()
            return render(request,"libros.html",{"libros":libros})
           
    else:
        mi_formulario=Libros_formulario(initial={'titulo':libros.titulo,'año':libros.año,'nombreautor':libros.nombreautor,'apellidoautor':libros.apellidoautor,'genero':libros.genero,'precio':libros.precio})
        
    return render (request, "editarlibros.html", {"mi_formulario":mi_formulario, "libros":libros})

def editarvinilos (request,id):
    vinilos=Vinilos.objects.get (id=id)
    if request.method=="POST":
        mi_formulario=Vinilos_formulario(request.POST)
        if mi_formulario.is_valid():
            datos=mi_formulario.cleaned_data
            vinilos.artista=datos['artista']
            vinilos.añovinilo=datos['añovinilo']
            vinilos.nombrevinilo=datos['nombrevinilo']
            vinilos.preciovinilo=datos['preciovinilo']
            vinilos.save()
            
            vinilos=Vinilos.objects.all()
            return render(request,"vinilos.html",{"vinilos":vinilos})
    else:
        mi_formulario=Vinilos_formulario(initial={'artista':vinilos.artista,'añovinilo':vinilos.añovinilo,'nombrevinilo':vinilos.nombrevinilo,'preciovinilo':vinilos.preciovinilo})
        
    return render (request, "editarvinilos.html", {"mi_formulario":mi_formulario, "vinilos":vinilos})


def login_request(request):
    if request.method=="POST":

        form=AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario= form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")

            user= authenticate(username= usuario, password=contra)
            
            if user is not None: 
                login(request,user)
                avatares=Avatar.objects.filter(user=request.user.id)
                return render (request, "inicio.html")
                #return render (request, "inicio.html", {"url":avatares[0].imagen.url})

        
            else:
                return HttpResponse ("Usuario incorrecto")

        else:
            return HttpResponse(f"FORM INCORRECTO {form}")

    

    form= AuthenticationForm()
    return render  (request, "login.html", {"form":form})


def register (request):
    
    if request.method== "POST":
        form= UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render (request, "bienvenidapostregister.html")


    else:
        form=UserCreationForm()
    return render (request, "registro.html", {"form":form})




@login_required
def editarPerfil(request):
    
    usuario=request.user

    if request.method== "POST":
        
        miFormulario= UserEditForm(request.POST)

        if miFormulario.is_valid():
            informacion= miFormulario.cleaned_data

            usuario.email = informacion ['email']
            password = informacion ['password1']
            usuario.set_password(password)
            usuario.save()

            return render (request,  "inicio.html")


    else:
        miFormulario= UserEditForm(initial= {'email':usuario.email})
    
    return render (request, "editar_perfil.html", {"miFormulario":miFormulario, "usuario":usuario})


        

def mensajes_formulario(request):
    if request.method=="POST":

        mi_formulario=Mensajes_formulario(request.POST)

        if mi_formulario. is_valid():
            datos=mi_formulario.cleaned_data

            
            listamensajes=Mensajes(usuariomensaje=datos['usuariomensaje'], comentario=datos['comentario'])
            listamensajes.save()
            

            return render (request, "mensajes.html")

    return render (request,"mensajes.html")            


def eliminamensajes (request,id):

    listamensajes=Mensajes.objects.get(id=id)
    listamensajes.delete()

    listamensajes=Mensajes.objects.all()

    return render(request,"listamensajes.html", {"listamensajes":listamensajes})


def editarmensajes (request,id):
    listamensajes=Mensajes.objects.get (id=id)
    if request.method=="POST":
        mi_formulario=Mensajes_formulario(request.POST)
        if mi_formulario.is_valid():
            datos=mi_formulario.cleaned_data
            listamensajes.usuariomensaje=datos['usuariomensaje']
            listamensajes.comentario=datos['comentario']
            listamensajes.save()

            listamensajes=Mensajes.objects.all()
            return render(request,"listamensajes.html",{"listamensajes":listamensajes})
           
    else:
        mi_formulario=Mensajes_formulario(initial={'usuariomensaje':listamensajes.usuariomensaje,'comentario':listamensajes.comentario})
        
    return render (request, "editarmensajes.html", {"mi_formulario":mi_formulario, "listamensajes":listamensajes})



@login_required
def listamensajes(request):
    listamensajes=Mensajes.objects.all()
    dicc={"listamensajes":listamensajes}
    plantilla=loader.get_template("listamensajes.html")
    documento=plantilla.render(dicc)
    return HttpResponse(documento)

    return HttpResponse(listamensajes)