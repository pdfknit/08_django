import datetime
import random
from django.conf.global_settings import MEDIA_ROOT
from .models import Product, ProductCategory
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage
from functools import lru_cache
from django.views.decorators.cache import never_cache, cache_page
from django.conf import settings
from django.core.cache import cache

NOW = datetime.datetime.now()



def get_all_products():
    if settings.LOW_CACHE:
        KEY = 'all_products'
        all_products = cache.get(KEY)
        if not all_products:
            all_products = ProductCategory.objects.all()
            cache.set(KEY, all_products)
        return all_products
    else:
        return ProductCategory.objects.all()


def get_all_productcategory():
    if settings.LOW_CACHE:
        KEY = 'all_categories'
        categories = cache.get(KEY)
        if not categories:
            categories = ProductCategory.objects.all()
            cache.set(KEY, categories)
        return categories
    else:
        return ProductCategory.objects.all()


def main(request):
    all_products = get_all_products()[:3]
    return render(request, 'mainapp/index.html', context={
        'title': 'Главная',
        'today': NOW,
        'products': all_products,
    })


@never_cache
def products(request):
    cat_menu = get_all_productcategory()
    products = get_all_products()[:4]
    hot = get_hot_product(Product.objects.all())
    # basket = BasketManager(user=)

    return render(request, 'mainapp/products.html', context={
        'title': 'Продукты',
        'products': products[:4],
        'cat_menu': cat_menu,
        'media_root': MEDIA_ROOT,
        'hot': hot,
    })


@lru_cache
def get_hot_product(products):
    return random.choice(products)

# @cache_page(3600)
def contact(request):
    return render(request, 'mainapp/contact.html', context={
        'title': 'Контакты',
    })


@never_cache
def product(request, pk):
    title = 'продукты'
    cat_menu = get_all_productcategory()

    content = {
        'title': title,
        'links_menu': get_all_productcategory(),
        'product': get_object_or_404(Product, pk=pk),
        'cat_menu': cat_menu,
        # 'basket': get_basket(request.user),
    }

    return render(request, 'mainapp/product.html', content)


def category(request, pk, page=1):
    categories_menu = get_all_productcategory()
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
