from django.shortcuts import render
from webapp.models import Product
from django.shortcuts import render, get_object_or_404, redirect


def index_view(request, *args, **kwargs):
    products = Product.objects.all()
    return render(request, 'index.html', context={
        'products':products
    })


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product.html', context={
        'product': product
    })

# Create your views here.
