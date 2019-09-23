from django.shortcuts import render
from webapp.models import Product, category
from django.shortcuts import render, get_object_or_404, redirect
from webapp.forms import ProductForm


def index_view(request, *args, **kwargs):
    products = Product.objects.exclude(count=0).order_by('name')
    return render(request, 'index.html', context={
        'products': products,
        'category': category

    })


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product.html', context={
        'product': product,
        'category': category
    })


def add_product(request):
    if request.method == 'GET':
        form = ProductForm()
        return render(request, 'add_product.html', context={
            'form': form,
            'category': category
        })
    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            product = Product.objects.create(name=data['name'], description=data['description'],
                                             category=data['category'], count=data['count'], price=data['price'])
            return redirect('product_view', pk=product.pk)
        else:
            return render(request, 'add_product.html', context={
                'form': form,
                'category': category
                })


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'product': product})
    elif request.method == 'POST':
        product.delete()
        return redirect('index')


def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        form = ProductForm(data={'name': product.name, 'description': product.description, 'category': product.category,
                                 'count': product.count, 'price': product.price})
        return render(request, 'update.html', context={'form': form, 'product': product})
    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            product.name = data['name']
            product.description = data['description']
            product.category = data['category']
            product.count = data['count']
            product.price = data['price']
            product.save()
            return redirect('product_view', pk=product.pk)
        else:
            return render(request, 'update.html', context={'form': form, 'product': product})


def product_search(request):
    search = request.GET.get('search')
    lists = Product.objects.filter(name__contains=search)
    return render(request, 'search.html', context={
        'lists': lists,
        'category': category
    })


def product_category(request, cat):
    products = get_object_or_404(Product, category=cat)
    print(cat)
    print(product.category)
    product = Product.objects.filter(category__contains=category)
    print(product.category)
    return render(request, 'category.html', context={
        'category': category,
        'products': products,
        'product': product
    })
# Create your views here.
