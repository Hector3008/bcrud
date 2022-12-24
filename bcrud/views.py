from django.shortcuts import render
from django.http import HttpResponse
from bcrud.models import Autor, Entrada, Comentario, Categoria
from django.core import serializers

#testeos básicos

  #ejemplo de httpresponse
def hr(request):
  return HttpResponse("Esto es una vista que sirve como ejemplo de httpresponse")
  #ejemplo básico de render
def r(request):
  return render(request, "bcrud/test.html")
  #render a padre
def padre(request):
  return render(request, "bcrud/padre.html")

#testeos importantes
  
  #render a inicio
def inicio(request):
  entradas = Entrada.objects.all()
  return render(request, "bcrud/inicio.html",{"entradas":entradas})

#APIS
def autoresapi(request):
  autorestodos = Autor.objects.all()
  print(autorestodos)
  return HttpResponse(serializers.serialize('json',autorestodos))

def entradasapi(request):
  entradastodos = Autor.objects.all()
  print(entradastodos)
  return HttpResponse(serializers.serialize('json',entradastodos))

def comentariosapi(request):
  comentariostodos = Comentario.objects.all()
  print(comentariostodos)
  return HttpResponse(serializers.serialize('json', comentariostodos))

def categoriasapi(request):
  categoriastodas = Categoria.objects.all()
  print(categoriastodas)
  return HttpResponse(serializers.serialize('json', categoriastodas))


#busquedas
def buscarautores(request):
  return render(request,"bcrud/busquedaautores.html")

def buscar(request):
  nombreview=request.GET['nombre']
  descripciones = Autor.objects.filter(nombre=nombreview)
  return render(request,"bcrud/resultadoautores.html",{"nombre":nombreview,"descripciones":descripciones})


#CRUD autores

from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView


class AutorList(ListView):
  model = Autor
  template_name="bcrud/autor_list.html"

class AutorCreacion(CreateView):
  model = Autor
  fields= '__all__'
  success_url= '/bcrud/autor/list'

class AutorEdicion(UpdateView):
  model = Autor
  fields= '__all__'
  success_url= '/bcrud/autor/list'

class AutorDetalle(DetailView):
  model = Autor
  template_name="bcrud/autor_detail.html"

class AutorBorrar(DeleteView):
  model = Autor
  success_url= '/bcrud/autor/list'

#CRUD entradas

class EntradaList(ListView):
  model = Entrada
  template_name="bcrud/entrada_list.html"

class EntradaCreacion(CreateView):
  model = Entrada
  fields= '__all__'
  success_url= '/bcrud/entrada/list'

class EntradaEdicion(UpdateView):
  model = Entrada
  fields= '__all__'
  success_url= '/bcrud/entrada/list'

class EntradaDetalle(DetailView):
  model = Entrada
  template_name="bcrud/entrada_detail.html"

class EntradaBorrar(DeleteView):
  model = Entrada
  success_url= '/bcrud/entrada/list'

#CRUD comentarios
class ComentarioList(ListView):
  model = Comentario
  template_name="bcrud/comentario_list.html"

class ComentarioCreacion(CreateView):
  model = Comentario
  fields= '__all__'
  success_url= '/bcrud/comentario/list'

class ComentarioEdicion(UpdateView):
  model = Comentario
  fields= '__all__'
  success_url= '/bcrud/comentario/list'

class ComentarioDetalle(DetailView):
  model = Comentario
  template_name="bcrud/comentario_detail.html"

class ComentarioBorrar(DeleteView):
  model = Comentario
  success_url= '/bcrud/comentario/list'

#CRUD categoria
class CategoriaList(ListView):
  model = Categoria
  template_name="bcrud/categoria_list.html"


class CategoriaCreacion(CreateView):
  model = Categoria
  fields= '__all__'
  success_url= '/bcrud/categoria/list'

class CategoriaEdicion(UpdateView):
  model = Categoria
  fields= '__all__'
  success_url= '/bcrud/categoria/list'

class CategoriaDetalle(DetailView):
  model = Categoria
  template_name="bcrud/categoria_detail.html"

class CategoriaBorrar(DeleteView):
  model = Categoria
  success_url= '/bcrud/categoria/list'