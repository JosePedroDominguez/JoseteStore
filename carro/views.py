from productoApp.models import Items

from django.shortcuts import redirect

from .carro import Carro
# Create your views here
def agregar_producto(request, id):

    carro=Carro(request)

    producto=Items.objects.get(id=id)

    carro.agregar(producto=producto)

    return redirect("caja")


def eliminar_producto(request, producto_id):

    carro=Carro(request)

    producto=Items.objects.get(id=producto_id)


    carro.eliminar(producto=producto)

    return redirect("caja")


def restar_producto(request, producto_id):

    carro=Carro(request)

    producto=Items.objects.get(id=producto_id)

    carro.restar_producto(producto=producto)

    return redirect("caja")

def cart_clear(request):
   carro=Carro(request)
   carro.cart_clear()
   return redirect("caja")