from django import forms


class ClienteForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    edad = forms.IntegerField()
    email = forms.EmailField()


class BusquedaClienteForm(forms.Form):
    nombre = forms.CharField()


class ProductoForm(forms.Form):
    nombre = forms.CharField()
    precio = forms.DecimalField()
    stock = forms.IntegerField()


class DetalleDeCompraForm(forms.Form):
    cantidad = forms.IntegerField()
    fecha_compra = forms.DateField()
    direccion = forms.CharField()


class CuponDeNavidadForm(forms.Form):
    codigo = forms.IntegerField()
    valido = forms.BooleanField()
