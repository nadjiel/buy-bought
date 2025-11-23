from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Defines functions that execute in response to requests

# products = [
#     {'name': 'Pair of boots'},
#     {'name': 'Old IPhone'},
#     {'name': 'Almost new couch'},
# ]


def get_products(request):
    if request.method == "GET":
        products = Product.objects.all()

        # Renders template from templates folder
        return render(request, 'products.html', {'products': products})
    elif request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")

        product = Product(
            name=name,
            price=price,
        )

        product.save()

        return HttpResponse({
            'name': name,
            'price': price,
        })


def get_product(request):
    if request.method == "GET":
        return HttpResponse('GET PRODUCT!')
    elif request.method == "POST":
        return HttpResponse('POST PRODUCT!')


def new_product(request):
    return render(request, 'new.html')
