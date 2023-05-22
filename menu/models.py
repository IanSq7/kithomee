from django.db import models

# Create your models here.

class Venta(models.Model):
    idVenta = models.AutoField(primary_key=True, verbose_name='Código de venta')
    nombreVenta = models.CharField (max_length=40)
    fechaVenta = models.DateField ()
    total = models.IntegerField ()
    fechaDespacho = models.DateField ()
    fechaEntrega = models.DateField ()
    estado = models.CharField (max_length= 100)
    costoDespacho= models.IntegerField ()
    carrito = models.IntegerField ()
    idUsuario = models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)



class Usuario(models.Model):
    idUsuario = models.AutoField (primary_key=True, verbose_name= 'Código de usuario' )
    nombre= models.CharField (max_length=100)
    apellido = models.CharField (max_length=100)
    correo = models.EmailField (max_length= 150)
    telefono = models.IntegerField ()
    fechaNacimiento = models.DateField ()
    respuesta = models.CharField (max_length=100)
    idRol = models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)
    idPregunta = models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)



class PreguntaSecreta (models.Model):
    idPregunta = models.AutoField (primary_key=True, verbose_name= 'Código de pregunta' )



class Rol (models.Model):
    idRol = models.AutoField (primary_key=True, verbose_name= 'Código de rol' ) 
    nombre = models.CharField (max_length=100)


class Direccion (models.Model):
    idDireccion = models.AutoField (primary_key=True, verbose_name= 'Código de direccion' )
    calle = models.CharField (max_length=100)
    numero = models.Number ()
    descripcion = models.CharField (max_length=100)
    codigoPostal = models.IntegerField ()
    idUsuario = models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)
    idComuna = models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)



class Comuna (models.Model):
    idComuna = models.AutoField (primary_key=True, verbose_name= 'Código de comuna' )
    nombreComuna = models.CharField (max_length=100)
    idRegion = models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)



class Region (models.Model):
    idRegion = models.AutoField (primary_key=True, verbose_name='Código region')
    nombre = models.CharField (max_length=100)


class Despacho (models.Model):
    idDespacho = models.AutoField (primary_key=True, verbose_name='Código de despacho')
    costo = models.IntegerField ()


class Detalle (models.Model):
    idDetalle = models.AutoField (primary_key=True, verbose_name='Código de detalles')
    cantidad = models.IntegerField ()
    subtotal = models.CharField (max_length=100)
    idVenta = models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)
    idProducto = models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)


class Producto (models.Model):
    idProducto = models.AutoField (primary_key=True, verbose_name='Código de producto')
    nombre = models.CharField (max_length=100)
    descripcion = models.CharField (max_length=100)
    precio = models.IntegerField ()
    estado = models.CharField (max_length=50)
    foto = models.ImageField 
    stock = models.IntegerField ()


class Categoria (models.Model):
    idCategoria = models.AutoField (primary_key=True , verbose_name= 'Código de categoria')
    nombre = models.CharField (max_length=100)

