from django.db import models


class Category(models.Model):
    """
    Category model
    """
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
    """
    Product model
    """
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    image = models.ImageField(null=True, blank=False)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Size(models.Model):
    """
    Size model
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Paper(models.Model):
    """
    Paper model
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ProductSpec(models.Model):
    """
    Product specs model
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(null=True, default=0)
    objects = models.Manager()

    def __str__(self):
        return self.product.name
