from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('product/<int:id>', views.product_detail, name='product_detail'),
    path('add-to-cart', views.add_to_cart, name='add_to_cart'),
    path('add/', views.add_product, name='add_product'),
    path('add-spec/', views.add_product_spec, name='add_product_spec'),
]


