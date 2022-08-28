from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('update-cart', views.update_cart, name='update_cart'),
]