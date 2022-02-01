import datetime

from django.conf.global_settings import MEDIA_ROOT

from .models import Product, ProductCategory
from django.shortcuts import render, get_object_or_404
# from ..geekshop.settings import MEDIA_ROOT

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

    return render(request, 'mainapp/products.html', context={
        'title': 'Продукты',
        'menu_links': MENU_LINKS,
        'products': products,
        'cat_menu': cat_menu,
        'media_root': MEDIA_ROOT,
    })


def contact(request):
    return render(request, 'mainapp/contact.html', context={
        'title': 'Контакты',
        'menu_links': MENU_LINKS,
    })


def category(request, pk):
    cat_menu = ProductCategory.objects.all()
    category = get_object_or_404(ProductCategory, pk=pk)
    products = Product.objects.filter(category=category)

    return render(request, 'mainapp/products.html', context={
        'title': 'Продукты',
        'menu_links': MENU_LINKS,
        'products': products,
        'cat_menu': cat_menu,
        'media_root': MEDIA_ROOT,
    })
