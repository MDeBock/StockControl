from django.contrib import admin
from compra.models import *


class ProductoAdmin(admin.ModelAdmin):
    model = Producto
    list_display = ("id", "nombre", "precio", "stock_actual", "proveedor")
    
    
    
class ProveedorAdmin(admin.ModelAdmin):
    model = Proveedor
    list_display = ("id", "nombre", "apellido", "dni")




admin.site.register(Producto, ProductoAdmin)
admin.site.register(Proveedor, ProveedorAdmin)