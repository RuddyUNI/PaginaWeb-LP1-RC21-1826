from django.db import models

# Create your models here.
class productos(models.Model):
    codigoProducto = models.IntegerField()
    descripcionProducto = models.CharField(max_length=255)
    estatus = models.BooleanField()

    def estatus_display(self):
        return "Disponible" if self.estatus else "No disponible"