from django.shortcuts import render, get_object_or_404
from mainapp.models import Product, ProductCategory


def product_create(request):
    pass

def product_read(request):
    pass

def products(request, pk):
    category = get_object_or_404(ProductCategory, pk=pk)
    products = Product.objects.filter(category_id=category).order_by('id')

    return render(request, 'adminapp/products.html', context={
        'title': 'Продукты',
        'category':category,
        'objects': products,
    })


def product_update(request):
    pass


def product_delete(request, pk):
    pass
