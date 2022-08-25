from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('product/<int:id>', views.product_detail, name='product_detail'),
    path('add-to-cart', views.add_to_cart, name='add_to_cart'),
]


