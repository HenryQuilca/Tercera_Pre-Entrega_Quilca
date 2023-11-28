# Proyecto Coder: 3ra Pre-Entrega:

## 1ro) Creación del proyecto:
### - **Se creó el repositorio a partir de una venta de Git Bash.** 
##### 1.  En la ventana de Git Bush debemos asegurarmos de estar en la carpeta que donde vamos a crear nuestro repositorio, en este caso la carpeta es PycharmProjects, por lo cual escribimos el siguiente comando para pasar a esa carpeta:
**`cd PycharmProjects/`**

![](https://i.ibb.co/G7QcdGW/Captura-de-pantalla-2023-11-28-095838.png)

##### 2. Luego procedemos a instalar Django,  ecribimos el comando `pip install django`, si queremos verificar que se instaló correctamente, escribimos `django-admin --version`.
##### 3. Finalmente crearemos el proyecto que tendrá de nombre Tercera_PreEntrega_Quilca, para ello escribimos el siguiente comando: `django-admin startproject Tercera_PreEntrega_Quilca`
##### 4. Ahora si tendremos el repositorio creado en nuestra computadora.

## 2do) Codificación en Repositorio:
##### 1. Abrimos nuestro repositorio en PyCharm y debemos crear un entorno virtual: Python Interpreter --> Add new interpreter --> Add Local Interpreter, se abrirá una ventana donde debe estar el python de pyenv. Para verificar abrimos un nuevo terminal y debe aparecer (venv).
![](https://i.ibb.co/TLbvRS7/Captura-de-pantalla-2023-11-28-102530.png)
En pycharm debemos de instalar de nuevo Django ya que es un entorno totalmente diferente.
##### 2. Concluimos escribiendo los siguientes comandos en la terminal:
`python manage.py migrate`
`python manage.py runserver`
##### 3. Luego escribimos el comando `python manage.py startapp App3raPreEntrega` esta será la carpeta donde trabajaremos la mayoría del tiempo.
##### 4. Dentro de la carpeta App3raPreEntrega encontramos el archivo "models.py", dentro debemos crear nuestras clases.
![](https://i.ibb.co/vYGZBvK/Captura-de-pantalla-2023-11-28-104219.png)
![](https://i.ibb.co/NYp1JC8/Captura-de-pantalla-2023-11-28-104336.png)
##### 5. Con las clases ya creadas debemos crear nuesta aplicación dentro de las configuración para que puedan ser leídas, abrimos el archivo settings.py y buscamos INSTALLED_APPS, en ese apartado agregagos lo siguiente: `'App3raPreEntrega',`
![](https://i.ibb.co/NjBzVkk/Captura-de-pantalla-2023-11-28-105625.png)
##### 6. Luego en la terminal escribimos el comando `python manage.py makemigrations` , este comando se debe ejecutar cada vez que hagamos un cambio en el archivo models.py y luego corremos el comando `python manage.py migrate`.
##### 7. Ahora continuamos creando las vistas, estas se ubicaran en el archivo "views.py".
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
##### 8. Recordemos que nos ayudamos de una plantilla base, la cual hereda a las demás plantillas creadas para cada vista, esto se ve en el repositorio subido.
##### 9. Recordemos que para cada vista tambien debe tener su URL.
![](https://i.ibb.co/J3dqfvf/Captura-de-pantalla-2023-11-28-110940.png)
##### 10. Toda la codificación se encuentra subida al repositorio de GITHUB.

## 3ro) Probando el proyecto:
##### 1. Cuando ejecutamos el proyecto nos proporciona un link, a este link le agregamos /app/ y no llevará automáticamente a la página.
[http://127.0.0.1:8000/app/](http://127.0.0.1:8000/app/)
##### 2. Dentro podremos observar 6 botones que nos redirigen a las funciones o vistas que hemos creado:
![](https://i.ibb.co/Ht9X1gH/Captura-de-pantalla-2023-11-28-111730.png)
- **Tiendita de Miku:** Este botón no redirige a la página principal.
- **Cliente:** Al dar clic en el botón "Cliente" no redirige a un formulario donde ingresaremos los datos que nos piden para que sen guardados en la base de datos. Si llenamos los recuadros y damos clic en "CrearCliente", automáticamente no redigirá a la url de mostrar clientes ahí aparecerá todos los clientes creados hasta el momento.
![](https://i.ibb.co/GQJp94n/Captura-de-pantalla-2023-11-28-112108.png)

------------
![](https://i.ibb.co/QJWTsVf/Captura-de-pantalla-2023-11-28-112315.png)
- **Producto:** Este botón también te redirige a su propio formulario y al crear el producto también te muestra los productos creados. 
![](https://i.ibb.co/PmN7bgz/Captura-de-pantalla-2023-11-28-112810.png)

------------

![](https://i.ibb.co/gDVB45F/Captura-de-pantalla-2023-11-28-112918.png)
- **Los botones "Cupón de Descuento" y "Detalle su compra" tienen la misma funcionalidad que los botones anteriormente descritos.** 
- **Buscar Cliente:** En este botón al darle clic nos aparecerá la lista completa de todos los clientes creado acompañado de un formulario donde podemos ingresar los caracteres que queremos buscar del nombre de cada cliente.
![](https://i.ibb.co/q1yFKPp/Captura-de-pantalla-2023-11-28-113347.png)
