from django.urls import path

from productoApp.views import Pantalla_de_Producto, Pantalla_de_Cargar_Producto, listarItems, Editar, Borrar, categorias, marca, Resultado_de_Busqueda, categoriasfiltradas, marcasFiltradas, CargaMarca, Cargar_Categoria
urlpatterns = [
    ############### URLS de store###############
    path('PantallaProducto/<id>/', Pantalla_de_Producto,
         name="Pantalla de Producto"),
    path('Listar/', listarItems, name="Pantalla de Listar Productos"),
    path('Editar/<id>/', Editar, name="Editar Producto"),
    path('Borrar/<id>/', Borrar, name="Borar Producto"),
    path('PantallaCargaProducto/', Pantalla_de_Cargar_Producto,
         name="Pantalla de Cargar Producto"),
    path('Cargar_Categoria/', Cargar_Categoria, name="Cargar_Categoria"),
    path('CargaMarca/', CargaMarca, name="CargaMarca"),
    path('formularioItem/', Pantalla_de_Cargar_Producto, name="guardarItem"),
    path('ResultadoBusqueda/', Resultado_de_Busqueda,
         name="Resultado de Busqueda"),
    path('categorias/', categorias, name="categorias"),
    path('marcas/', marca, name="marcas"),
    path('categoriasfiltradas/<id>/',
         categoriasfiltradas, name="categoriasfiltradas"),
    path('marcasFiltradas/<id>/',
         marcasFiltradas, name="marcasFiltradas"),
    #####################################
]
