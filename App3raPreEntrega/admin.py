from django.contrib import admin
from App3raPreEntrega.models import Cliente, Producto, DetalleDeCompra, CuponDeNavidad

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(DetalleDeCompra)
admin.site.register(CuponDeNavidad)
