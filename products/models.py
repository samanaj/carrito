from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=300)
    featured = models.BooleanField(default= False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class Product(models.Model):
    name = models.CharField(max_length=300)
    #para colocar un codigo al producto un sku por ejemplo
    slug = models.SlugField()
    #fk que apunta al modelo a relacionar y on:delete para que borre en cascada todos los productos relacionados a esa categoria
    category = models.ForeignKey(Category, on_delete=models.CASCADE)    
    image = models.ImageField(upload_to='products/', blank=True)
    #un extracto corto de los datos del producto para mostrar en el template
    excerp = models.TextField(max_length=200, verbose_name='Extracto')
    detail = models.TextField(max_length=1000, verbose_name='Información del producto')
    price = models.FloatField()
    #producto diponible o no.
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'