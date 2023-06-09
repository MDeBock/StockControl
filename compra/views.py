from http.client import HTTPResponse
from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404,redirect
from django.http.response import JsonResponse

def index(request):

    return HTTPResponse("Hola mundo")

def nuevo_proveedor(request):

    if request.POST:

        Proveedor.objects.create(
            nombre = request.POST["nombre"],
            apellido = request.POST["apellido"],
            dni = request.POST["dni"],
        )
    return render(request,'compra/nuevo_proveedor.html')

def nuevo_producto(request):
    
    proveedores = Proveedor.objects.all()
    
    context = {
        "proveedores": proveedores
    }
    
    if request.POST:
        nombre = request.POST['nombre']    
        precio = request.POST['precio'] 
        stock_actual = request.POST['stock_actual'] 
        proveedor_id = request.POST['proveedor']
        
        Producto.objects.create(
            nombre = nombre,
            precio = precio,
            stock_actual = stock_actual,
            proveedor_id = proveedor_id
        )
        
    return render(request, "compra/nuevo_producto.html", context)

def listado_proveedores(request):
    proveedores = Proveedor.objects.all()
    print(proveedores)
    context = {
        "proveedores": proveedores
    }
    return render(request, "compra/listado_proveedores.html", context)

def list_productos(_request):
    productos = list(Producto.objects.values())
    data = {'productos': productos}
    return JsonResponse(data)

def lista_productos(request):
    return render(request, 'compra/lista_productos.html')