import datetime

from django.shortcuts import render

from django.shortcuts import render

MENU_LINKS = {'домой': '', 'продукты': 'products', 'контакты': 'contact'}
NOW = datetime.datetime.now()

def main(request):
    return render(request, 'mainapp/index.html', context={
        'title': 'Главная',
        'menu_links': MENU_LINKS,
        'today': NOW,
    })


def products(request):
    cat_menu = {'все':'', 'дом':'','офис':'','модерн':'','классика':'',}
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
