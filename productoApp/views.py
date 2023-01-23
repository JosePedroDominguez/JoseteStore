
from django.core import paginator

from django.http.response import Http404

from django.shortcuts import render, redirect, get_object_or_404

from productoApp.forms import FomularioItem, FomularioTag, FormularioMarca

from productoApp.models import Items, Tag, Marca

from django.contrib import messages

from django.core.paginator import Paginator

from django.contrib.auth.decorators import permission_required
# Create your views here.


def Pantalla_de_Producto(request, id):
    it = Items.objects.filter(id=id)
    data = {
        'prod': it
    }
    return render(request, 'PantallaProducto.html', data)


@permission_required('productoApp.add_tag')
def Cargar_Categoria(request):  # SOLO VISIBLE PARA LOS ADMINISTRADORES
    data = {
        'form': FomularioTag()
    }
    if request.method == 'POST':
        form = FomularioTag(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Agregado Correctamante")
        else:
            data["form"] = form
    return (render(request, "Carga_Categoria.html", data))


@permission_required('productoApp.add_marca')
def CargaMarca(request):  # SOLO VISIBLE PARA LOS ADMINISTRADORES
    data = {
        'form': FormularioMarca()
    }
    if request.method == 'POST':
        form = FormularioMarca(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Agregado Correctamante")
        else:
            data["form"] = form
    return (render(request, "CargaMarca.html", data))


@permission_required('productoApp.add_items')
# SOLO VISIBLE PARA LOS ADMINISTRADORES
def Pantalla_de_Cargar_Producto(request):
    data = {
        'form': FomularioItem()
    }
    if request.method == 'POST':
        formulario = FomularioItem(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Cargado Correctamante")
        else:
            data["form"] = formulario
    return (render(request, "CargaDeProducto.html", data))


@permission_required('productoApp.view_items')
def listarItems(request):  # SOLO VISIBLE PARA LOS ADMINISTRADORES
    itms = Items.objects.all()
    page = request.GET.get('page', 1)  # paginacion

    try:
        paginator = Paginator(itms, 5)
        itms = paginator.page(page)
    except:
        raise Http404
    data = {
        'entity': itms,
        'paginator': paginator
    }

    return (render(request, "adminItems.html", data))


@permission_required('productoApp.change_items')
def Editar(request, id):  # SOLO VISIBLE PARA LOS ADMINISTRADORES
    prod = get_object_or_404(Items, id=id)
    data = {
        'form': FomularioItem(instance=prod)
    }
    if request.method == 'POST':
        formulario = FomularioItem(
            data=request.POST, instance=prod, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Editado Correctamante")
            return (redirect(to="Pantalla de Listar Productos"))
        else:
            data["form"] = formulario
    return render(request, "editItem.html", data)


@permission_required('productoApp.delete_items')
def Borrar(request, id):  # SOLO VISIBLE PARA LOS ADMINISTRADORES
    prod = get_object_or_404(Items, id=id)
    prod.delete()
    messages.success(request, "Eliminado Correctamante")
    return (redirect(to="Pantalla de Listar Productos"))


def Resultado_de_Busqueda(request):
    itm = Items.objects.all()
    data = {
        'productos': itm
    }
    return (render(request, "Home.html", data))


def categorias(request):
    cat = Tag.objects.all()
    data = {
        'stf': cat
    }
    return (render(request, "categorias.html", data))

#### new####


def marca(request):
    mar = Marca.objects.all()
    data = {
        'fab': mar
    }
    return (render(request, "marcas.html", data))
#### new####


def categoriasfiltradas(request, id):
    category = Items.objects.filter(tag=id)
    return (render(request, "categoriasfiltradas.html", {'id': id, 'category': category}))


def marcasFiltradas(request, id):
    marca = Items.objects.filter(marca=id)
    return (render(request, "marcasFiltradas.html", {'id': id, 'marca': marca}))
