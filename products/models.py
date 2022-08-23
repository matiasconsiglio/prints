from django.db import models

# Create your models here.

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name

class Product(models.Model):

    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.name

class Size(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Paper(models.Model):
    
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ProductSpec(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(null=True, default=0)
    objects = models.Manager()

    def __str__(self):
        return self.product.name
