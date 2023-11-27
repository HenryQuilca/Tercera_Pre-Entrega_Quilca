from django.urls import path
from App3raPreEntrega.views import inicio, crear_cliente, mostrar_clientes, buscar, crear_producto, mostrar_productos, \
    crear_compra, mostrar_compra, crear_cupon, mostrar_cupon

urlpatterns = [
    path('', inicio),
    path('crear_cliente/', crear_cliente),
    path('buscar/', buscar),
    path('mostrar_clientes/', mostrar_clientes),
    path('crear_producto/', crear_producto),
    path('mostrar_productos/', mostrar_productos),
    path('crear_compra/', crear_compra),
    path('mostrar_compra/', mostrar_compra),
    path('crear_cupon/', crear_cupon),
    path('mostrar_cupon/', mostrar_cupon),
]
