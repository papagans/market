from django.shortcuts import render
from webapp.models import Product
from django.shortcuts import render, get_object_or_404, redirect
from webapp.forms import ProductForm


def index_view(request, *args, **kwargs):
    products = Product.objects.all()
    return render(request, 'index.html', context={
        'products': products
    })


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product.html', context={
        'product': product
    })


def add_product(request):
    if request.method == 'GET':
        form = ProductForm()
        return render(request, 'add_product.html', context={'form': form})
    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            product = Product.objects.create(name=data['name'], description=data['description'],
                                             category=data['category'], count=data['count'], price=data['price'])
            return redirect('product_view', pk=product.pk)
        else:
            return render(request, 'add_product.html', context={'form': form})


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'product': product})
    elif request.method == 'POST':
        product.delete()
        return redirect('index')
# Create your views here.
