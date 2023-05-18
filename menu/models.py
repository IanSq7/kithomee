from django.db import models

# Create your models here.

class Venta(models.Model):
    idVenta = models.AutoField(primary_key=True, verbose_name='Código de venta')
    nombreVenta = models.CharField (max_length=40)
    fechaVenta = models.DateField ()
    

