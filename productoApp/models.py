from django.db import models
# Create your models here.
class Tag(models.Model):
    nametag  = models.CharField(max_length=50)

    def __str__(self):
        return self.nametag
class Marca(models.Model):
    name  = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Items(models.Model):
    name = models.CharField(max_length=50)
    imag = models.ImageField( upload_to="productos", null=True)
    tag  = models.ForeignKey(Tag, on_delete= models.PROTECT)
    marca = models.ForeignKey(Marca, on_delete= models.PROTECT, null=True)
    description = models.TextField()
    price = models.FloatField()
    
    def __str__(self):
        return self.name


class ImagenProducto(models.Model):
    imagen = models.ImageField( upload_to="productos")
    items = models.ForeignKey(Items, on_delete=models.CASCADE, related_name="imagenes")