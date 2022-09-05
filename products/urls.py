from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('product/<int:id>', views.product_detail, name='product_detail'),
    path('add-to-cart', views.add_to_cart, name='add_to_cart'),
    path('add/', views.add_product, name='add_product'),
    path('add-spec/', views.add_product_spec, name='add_product_spec'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path(
        'delete/<int:product_id>/', views.delete_product, name='delete_product'
        ),
]
