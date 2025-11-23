from django.urls import path
from . import views

# Ties routes to views within this app
urlpatterns = [
    path('', views.get_products, name='products'),
    path('products/', views.get_product, name='get_product'),
    path('products/new', views.new_product, name='new_product'),
]
