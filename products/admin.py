from django.contrib import admin
from .models import Product, Category, ProductSpec, Size, Paper

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'image',
    )
    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class ProductSpecAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'size',
        'paper',
        'price',
    )
    ordering = ('product',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductSpec, ProductSpecAdmin)
admin.site.register(Size)
admin.site.register(Paper)
