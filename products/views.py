from django.shortcuts import render
from .models import Product


def all_products(request):
    """ A view to return the all product page """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/product_list.html', context)
