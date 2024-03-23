from django.db import models

# Create your models here.

class Tienda(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre.__str__()

class Producto(models.Model):
    nombre = models.CharField(max_length=100, null=True)
    variante = models.CharField(max_length=100, null=True)
    perecedero = models.BooleanField(default=True)
    tienda_id = models.ForeignKey(Tienda, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Precio(models.Model):
    producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE)
    tienda_id = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    precio = models.FloatField()
    fecha = models.DateField()
