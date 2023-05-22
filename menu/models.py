from django.db import models

# Create your models here.
class Rol (models.Model):
    idRol = models.AutoField (primary_key=True, verbose_name= 'Código de rol' ) 
    nombre = models.CharField (max_length=100)

class Pregunta (models.Model):
    idPregunta = models.AutoField (primary_key=True, verbose_name= 'Código de pregunta' )  
    nombre = models.CharField (max_length=100)


class Usuario(models.Model):
    idUsuario = models.AutoField (primary_key=True, verbose_name= 'Código de usuario' )
    nombre= models.CharField (max_length=100)
    apellido = models.CharField (max_length=100)
    correo = models.EmailField (max_length= 150)
    telefono = models.IntegerField ()
    fechaNacimiento = models.DateField ()
    respuesta = models.CharField (max_length=100)
    idRol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    idPregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)

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
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def _str_ (self) -> str:
        return self.nombreVenta


class Categoria (models.Model):
    idCategoria = models.AutoField (primary_key=True , verbose_name= 'Código de categoria')
    nombre = models.CharField (max_length=100)

    def _str_ (self) -> str:
        return self.nombre


class Region (models.Model):
    idRegion = models.AutoField (primary_key=True, verbose_name='Código region')
    nombre = models.CharField (max_length=100)

    def _str_ (self) -> str:
        return self.nombre

class Comuna (models.Model):
    idComuna = models.AutoField (primary_key=True, verbose_name= 'Código de comuna' )
    nombreComuna = models.CharField (max_length=100)
    idRegion = models.ForeignKey(Region, on_delete=models.CASCADE)

    def _str_ (self) -> str :
        return self.nombreComuna



class Direccion (models.Model):
    idDireccion = models.AutoField (primary_key=True, verbose_name= 'Código de direccion' )
    calle = models.CharField (max_length=100)
    numero = models.IntegerField ()
    descripcion = models.CharField (max_length=100)
    codigoPostal = models.IntegerField ()
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    idComuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)

    def _str_ (self) -> str :
        return self.calle



class Producto (models.Model):
    idProducto = models.AutoField (primary_key=True, verbose_name='Código de producto')
    nombre = models.CharField (max_length=100)
    descripcion = models.CharField (max_length=100)
    precio = models.IntegerField ()
    estado = models.CharField (max_length=50)
    foto = models.ImageField 
    stock = models.IntegerField ()
    idCategoria = models.ForeignKey (Categoria, on_delete=models.CASCADE)

    def _str_ (self) -> str:
        return self.nombre


class Despacho (models.Model):
    idDespacho = models.AutoField (primary_key=True, verbose_name='Código de despacho')
    costo = models.IntegerField ()


class Detalle (models.Model):
    idDetalle = models.AutoField (primary_key=True, verbose_name='Código de detalles')
    cantidad = models.IntegerField ()
    subtotal = models.CharField (max_length=100)
    idVenta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)





