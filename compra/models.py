from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(verbose_name="Nombre",max_length=50)
    apellido = models.CharField(verbose_name="Apellido",max_length=50)
    dni = models.IntegerField(verbose_name="dni")
    
    def __str__(self):
        return self.nombre
    

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField(default=0)
    stock_actual = models.IntegerField(verbose_name="stock actual")
    proveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE,related_name="producto")
    
