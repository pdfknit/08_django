import datetime

from .models import Product, ProductCategory

from django.shortcuts import render

MENU_LINKS = {'домой': '', 'продукты': 'products', 'контакты': 'contact'}
NOW = datetime.datetime.now()

def main(request):
    all_products = Product.objects.all()[:4]
    return render(request, 'mainapp/index.html', context={
        'title': 'Главная',
        'menu_links': MENU_LINKS,
        'today': NOW,
        'products': all_products,
    })


def products(request):
    # cat_menu = {'все':'', 'дом':'','офис':'','модерн':'','классика':'',}
    cat_menu = ProductCategory.objects.all()
    # products = Product.objects.all()
    products = [
        {
            'name': 'Лампа',
            'description' : 'Просто лампа',
            'image': 'img/product-11.jpg',
            '': '',
        },{
            'name': 'Стул',
            'description' : 'Отличный стул',
            'image': 'img/product-21.jpg',
            '': '',
        },{
            'name': 'Опять лампа',
            'description' : 'Лампа вашей мечты',
            'image': 'img/product-31.jpg',
            '': '',
        },{
            'name': 'Нечто',
            'description': 'Черного цвета',
            'image': 'img/product-51.jpg',
            '': '',
        }, {
            'name': 'Ваза',
            'description': 'Молочно-белая',
            'image': 'img/product-61.jpg',
            '': '',
        },

    ]
    return render(request, 'mainapp/products.html', context={
        'title': 'Продукты',
        'menu_links': MENU_LINKS,
        'products': products,
        'cat_menu': cat_menu
    })


def contact(request):
    return render(request, 'mainapp/contact.html', context={
        'title': 'Контакты',
        'menu_links': MENU_LINKS,
    })

def category(request, pk):
    return products(request)