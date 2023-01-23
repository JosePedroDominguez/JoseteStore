from django.http import request
from django.shortcuts import render
from productoApp.models import Items

#from django.contrib import messages
from productoApp.models import Tag

from django.http.response import Http404
from django.core.paginator import Paginator

from .forms import ContactoForm
from django.db.models import Q
# Create your views here.
def caja(request):
    productos=Items.objects.all()
    return render(request, "caja.html", {"productos":productos})

def Acera_de(request):

    return  render(request,'AcercaDe.html')
    
def Pantalla_Principal(request):
    #itm = Items.objects.all()
    itm = Items.objects.order_by('-id')
    page = request.GET.get('page',1)#paginacion

    try:
        paginator = Paginator(itm,9)
        itm = paginator.page(page)
    except:
        raise Http404
    data = {
        'entity': itm,
        'paginator':paginator,
    }
    return(render(request,"Home.html",data ))

def tags(request):
    cat = Items.objects.all()
    data={
        'dx': cat
    }
    return(render(request,"base.html",data ))

def Pantalla_de_Contacto(request):
    #return  render(request,'Contacto.html')
    data = {
        'form':ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "mensaje enviado exitosamente"
        else:
            data["form"] = formulario
    return render(request,'Contacto.html',data)
def buscar(request):
    if request.method == "POST":
        buscar = request.POST.get("buscar")
        prod = Items.objects.filter(name__icontains=buscar)
        return  render(request,'buscar.html',{'buscar':buscar, 'Items':prod})
    else:
        return  render(request,'buscar.html',{})


