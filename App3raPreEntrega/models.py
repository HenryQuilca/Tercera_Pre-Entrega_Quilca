from django.db import models


# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    edad = models.PositiveIntegerField()
    email = models.EmailField()

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}, Edad: {self.edad} años, email: {self.email} "


class Producto(models.Model):
    nombre = models.CharField(max_length=75)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return f"Producto: {self.nombre}, Precio: {self.precio} soles, Stock del producto: {self.stock} unidades"


class DetalleDeCompra(models.Model):
    cantidad = models.PositiveIntegerField()
    fecha_compra = models.DateField(auto_now_add=True)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return f"Unidades compradas: {self.cantidad}, Fecha de compra: {self.fecha_compra}"


class CuponDeNavidad(models.Model):
    codigo = models.PositiveIntegerField()
    valido = models.BooleanField()

    def __str__(self):
        return f"El código del cupon de Navidad: {self.codigo} "
