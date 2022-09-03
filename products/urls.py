from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('product/<int:id>', views.product_detail, name='product_detail'),
    path('add-to-cart', views.add_to_cart, name='add_to_cart'),
    path('add/', views.add_product, name='add_product'),
    path('add-spec/', views.add_product_spec, name='add_product_spec'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('edit-spec/<int:product_spec_id>/', views.edit_product_spec, name='edit_product_spec'),
]


