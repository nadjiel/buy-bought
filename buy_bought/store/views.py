from django.shortcuts import render
from django.http import HttpResponse

# Defines functions that execute in response to requests

products = [
    {'name': 'Pair of boots'},
    {'name': 'Old IPhone'},
    {'name': 'Almost new couch'},
]


def get_products(request):
    # Renders template from templates folder
    return render(request, 'products.html', {'products': products})


def get_product(request):
    return HttpResponse('Hello, World!')
