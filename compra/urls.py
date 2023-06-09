from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= "index"),
    path('proveedores/nuevo',views.nuevo_proveedor,name="nuevo_proveedor"),
    path('proveedores/listado', views.listado_proveedores, name="listado_proveedores"),
    path('productos/nuevo',views.nuevo_producto,name="nuevo_producto"),   
    path('productos/lista_productos/', views.lista_productos, name='lista_productos'),
    path('list_productos/', views.list_productos, name='list_productos'),
]