import datetime
import random
from django.conf.global_settings import MEDIA_ROOT
from .models import Product, ProductCategory
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage


NOW = datetime.datetime.now()


def main(request):
    all_products = Product.objects.all()[:5]
    return render(request, 'mainapp/index.html', context={
        'title': 'Главная',
        'today': NOW,
        'products': all_products,
    })


def products(request):
    cat_menu = ProductCategory.objects.all()
    products = Product.objects.all()[:3]
    hot = get_hot_product(Product.objects.all())
    # basket = BasketManager(user=)

    return render(request, 'mainapp/products.html', context={
        'title': 'Продукты',
        'products': products[:4],
        'cat_menu': cat_menu,
        'media_root': MEDIA_ROOT,
        'hot': hot,
    })


def get_hot_product(products):
    return random.choice(products)


def contact(request):
    return render(request, 'mainapp/contact.html', context={
        'title': 'Контакты',
    })


def product(request, pk):
    title = 'продукты'
    cat_menu = ProductCategory.objects.all()

    content = {
        'title': title,
        'links_menu': ProductCategory.objects.all(),
        'product': get_object_or_404(Product, pk=pk),
        'cat_menu': cat_menu,
        # 'basket': get_basket(request.user),
    }

    return render(request, 'mainapp/product.html', content)


def category(request, pk, page=1):
    categories_menu = ProductCategory.objects.all()
    category = get_object_or_404(ProductCategory, pk=pk)
    products = Product.objects.filter(category=category)
    paginator = Paginator(products, 3)

    try:
        products_page = paginator.page(page)
    except EmptyPage:
        products_page = paginator.page(paginator.num_pages)

    return render(request, 'mainapp/products.html', context={
        'title': 'Продукты',
        'products': products_page,
        'categories_menu': categories_menu,
        'media_root': MEDIA_ROOT,
        'hot': get_hot_product(products),
        'page': products_page,
        'paginator': paginator,
        'category': category,
    })
