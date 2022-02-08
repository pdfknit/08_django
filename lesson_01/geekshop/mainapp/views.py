import datetime
import random

from django.conf.global_settings import MEDIA_ROOT

from .models import Product, ProductCategory
from django.shortcuts import render, get_object_or_404

# from ..geekshop.settings import MEDIA_ROOT
# from ..basketapp.models import BasketManager

MENU_LINKS = {'домой': '', 'продукты': 'products', 'контакты': 'contact'}
NOW = datetime.datetime.now()


def main(request):
    all_products = Product.objects.all()[:5]
    return render(request, 'mainapp/index.html', context={
        'title': 'Главная',
        'menu_links': MENU_LINKS,
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
        'menu_links': MENU_LINKS,
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
        'menu_links': MENU_LINKS,
    })


def product(request, pk):
    title = 'продукты'
    cat_menu = ProductCategory.objects.all()

    content = {
        'title': title,
        'links_menu': ProductCategory.objects.all(),
        'product': get_object_or_404(Product, pk=pk),
        'menu_links': MENU_LINKS,
        'cat_menu': cat_menu,
        # 'basket': get_basket(request.user),
    }

    return render(request, 'mainapp/product.html', content)


def category(request, pk):
    cat_menu = ProductCategory.objects.all()
    category = get_object_or_404(ProductCategory, pk=pk)
    products = Product.objects.filter(category=category)

    return render(request, 'mainapp/products.html', context={
        'title': 'Продукты',
        'menu_links': MENU_LINKS,
        'products': products[:4],
        'cat_menu': cat_menu,
        'media_root': MEDIA_ROOT,
        'hot': get_hot_product(products),
    })
