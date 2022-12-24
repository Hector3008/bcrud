
from django.urls  import path
from bcrud  import views

urlpatterns = [
    #ejemplo de httpresponse
    path("hr/",views.hr),

    #ejemplo de render
    path("r/",views.r),

    #render a padre
    path("padre/",views.padre),
    #render a inicio
    path("inicio/",views.inicio,name='inicio'),

    #APIS
    path("autoresapi/",views.autoresapi, name='autoresapi'),
    path("entradasapi/",views.entradasapi, name='entradasapi'),
    path("comentariosapi/",views.comentariosapi, name='comentariosapi'),
    path("categoriasapi/",views.categoriasapi, name='categoriasapi'),

    #busquedas
    path("busquedaautores/",views.buscarautores, name='buscara'),
    path("buscar/",views.buscar,name="buscarau"),

    #CRUD autores
    path("autor/list/",views.AutorList.as_view(),name='alist'),
    path("autor/create/",views.AutorCreacion.as_view(),name='anew'),
    path("autor/edit/<pk>",views.AutorEdicion.as_view(),name='aedit'),
    path("autor/detail/<pk>",views.AutorDetalle.as_view(),name='adetail'),
    path("autor/delete/<pk>",views.AutorBorrar.as_view(),name='adelete'),

    #CRUD entradas
    path("entrada/list/",views.EntradaList.as_view(),name='elist'),
    path("entrada/create/",views.EntradaCreacion.as_view(),name='enew'),
    path("entrada/edit/<pk>",views.EntradaEdicion.as_view(),name='eedit'),
    path("entrada/detail/<pk>",views.EntradaDetalle.as_view(),name='edetail'),
    path("entrada/delete/<pk>",views.EntradaBorrar.as_view(),name='edelete'),

    #CRUD comentarios
    path("comentario/list/",views.ComentarioList.as_view(),name='clist'),
    path("comentario/create/",views.ComentarioCreacion.as_view(),name='cnew'),
    path("comentario/edit/<pk>",views.ComentarioEdicion.as_view(),name='cedit'),
    path("comentario/detail/<pk>",views.ComentarioDetalle.as_view(),name='cdetail'),
    path("comentario/delete/<pk>",views.ComentarioBorrar.as_view(),name='cdelete'),

    #CRUD comentarios
    path("categoria/list/",views.CategoriaList.as_view(),name='calist'),
    path("categoria/create/",views.CategoriaCreacion.as_view(),name='canew'),
    path("categoria/edit/<pk>",views.CategoriaEdicion.as_view(),name='caedit'),
    path("categoria/detail/<pk>",views.CategoriaDetalle.as_view(),name='cadetail'),
    path("categoria/delete/<pk>",views.CategoriaBorrar.as_view(),name='cadelete'),



]
