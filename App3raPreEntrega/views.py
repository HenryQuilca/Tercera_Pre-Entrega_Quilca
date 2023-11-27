from django.http import HttpResponse
from django.shortcuts import render, redirect
from App3raPreEntrega.models import Cliente, Producto, DetalleDeCompra, CuponDeNavidad
from App3raPreEntrega.forms import ClienteForm, BusquedaClienteForm, ProductoForm, DetalleDeCompraForm, \
    CuponDeNavidadForm


# Create your views here.
def inicio(request):
    contexto = {}
    return render(request, 'index.html', contexto)


def mostrar_clientes(request):
    clientes = Cliente.objects.all()
    contexto = {
        "clientes": clientes,
        "miFormulario": BusquedaClienteForm(),
    }
    return render(request, 'App3raPreEntrega/mostrar_clientes.html', contexto)


def crear_cliente(request):
    if request.method == "POST":
        cliente_formulario = ClienteForm(request.POST)
        if cliente_formulario.is_valid():
            informacion = cliente_formulario.cleaned_data
            cliente_crear = Cliente(nombre=informacion['nombre'], apellido=informacion['apellido'], edad=informacion['edad'], email=informacion['email'])
            cliente_crear.save()
            return redirect("/app/mostrar_clientes/")

    cliente_formulario = ClienteForm()
    contexto = {
        "miFormulario": cliente_formulario
    }
    return render(request, "App3raPreEntrega/clientes.html", contexto)


def buscar(request):     # Busqueda
    nombre = request.GET["nombre"]
    clientes = Cliente.objects.filter(nombre__icontains=nombre)
    contexto = {
        "clientes": clientes,
        "miFormulario": BusquedaClienteForm(),
    }
    return render(request, 'App3raPreEntrega/mostrar_clientes.html', contexto)


def crear_producto(request):
    if request.method == "POST":
        producto_formulario = ProductoForm(request.POST)
        if producto_formulario.is_valid():
            informacion = producto_formulario.cleaned_data
            producto_crear = Producto(nombre=informacion['nombre'], precio=informacion['precio'], stock=informacion['stock'])
            producto_crear.save()
            return redirect("/app/mostrar_productos/")

    producto_formulario = ProductoForm()
    contexto = {
        "miFormulario": producto_formulario
    }
    return render(request, "App3raPreEntrega/productos.html", contexto)


def mostrar_productos(request):
    productos = Producto.objects.all()
    contexto = {
        "productos": productos,
        # "miFormulario": BusquedaClienteForm(),
    }
    return render(request, 'App3raPreEntrega/mostrar_productos.html', contexto)


def crear_compra(request):
    if request.method == "POST":
        compra_formulario = DetalleDeCompraForm(request.POST)
        if compra_formulario.is_valid():
            informacion = compra_formulario.cleaned_data
            compra_crear = DetalleDeCompra(cantidad=informacion['cantidad'], fecha_compra=informacion['fecha_compra'], direccion=informacion['direccion'])
            compra_crear.save()
            return redirect("/app/mostrar_compra/")

    compra_formulario = DetalleDeCompraForm()
    contexto = {
        "miFormulario": compra_formulario
    }
    return render(request, "App3raPreEntrega/compras.html", contexto)


def mostrar_compra(request):
    compras = DetalleDeCompra.objects.all()
    contexto = {
        "compras": compras,
    }
    return render(request, 'App3raPreEntrega/mostrar_detalle_compra.html', contexto)


def crear_cupon(request):
    if request.method == "POST":
        cupon_formulario = CuponDeNavidadForm(request.POST)
        if cupon_formulario.is_valid():
            informacion = cupon_formulario.cleaned_data
            cupon_crear = CuponDeNavidad(codigo=informacion['codigo'], valido=informacion['valido'])
            cupon_crear.save()
            return redirect("/app/mostrar_cupon/")

    cupon_formulario = CuponDeNavidadForm()
    contexto = {
        "miFormulario": cupon_formulario
    }
    return render(request, "App3raPreEntrega/cupones.html", contexto)


def mostrar_cupon(request):
    cupones = CuponDeNavidad.objects.all()
    contexto = {
        "cupones": cupones,
    }
    return render(request, 'App3raPreEntrega/mostrar_cupones.html', contexto)
