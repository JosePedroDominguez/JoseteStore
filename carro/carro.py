from django.conf import settings


class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get("carro")
        if not carro:
            carro = self.session["carro"] = {}
        self.carro = carro

    def agregar(self, producto):
        if (str(producto.id) not in self.carro.keys()):
            self.carro[producto.id] = {
                "producto_id": producto.id,
                "nombre": producto.name,
                "precio": str(producto.price),
                "cantidad": 1

            }
        else:
            for key, value in self.carro.items():
                if key == str(producto.id):
                    value["cantidad"] = value["cantidad"]+1
                    value["precio"] = float(value["precio"])+producto.price
                    break
        self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"] = self.carro
        self.session.modified = True

    def eliminar(self, producto):
        producto.id = str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()

    def restar_producto(self, producto):
        for key, value in self.carro.items():
            if key == str(producto.id):
                value["cantidad"] = value["cantidad"]-1
                value["precio"] = float(value["precio"])-producto.price
                if value["cantidad"] < 1:
                    self.eliminar(producto)
                break
        self.guardar_carro()

    def cart_clear(self):
        self.session["carro"] = {}
        self.session.modified = True
