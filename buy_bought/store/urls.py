from django.urls import path
from . import views

# Ties routes to views within this app
urlpatterns = [
    path('', views.get_products, name='get_products'),
    path('product', views.get_product, name='get_product'),
]
