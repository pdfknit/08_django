from django.conf import settings
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from functools import lru_cache
from basketapp.models import Basket
from mainapp.models import Product
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.core.cache import cache


def basket_objects_filter(user):
    if settings.LOW_CACHE:
        KEY = 'basket_objects_filter'
        basket_objects = cache.get(KEY)
        if not basket_objects:
            basket_objects = Basket.objects.filter(user=user)
            cache.set(KEY, basket_objects)
        return basket_objects
    else:
        return Basket.objects.filter(user=user)


def get_basket_objects(pk):
    if settings.LOW_CACHE:
        KEY = 'get_basket_objects'
        basket_objects = cache.get(KEY)
        if not basket_objects:
            basket_objects = Basket.objects.get(pk=pk)
            cache.set(KEY, basket_objects)
        return basket_objects
    else:
        return Basket.objects.get(pk=pk)


@login_required()
def basket(request):
    content = {}
    return render(request, 'basketapp/basket.html', context={
        'basket': basket_objects_filter(request.user),
        'title': 'Корзина',
    })


def add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    basket = Basket.objects.filter(user=request.user, product=product).first()

    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.save()
    basket.quantity += 1
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def remove(request, pk):
    basket = get_basket_objects(pk)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def edit(request, pk, quantity):
    new_basket_item = get_basket_objects(pk)
    if quantity > 0:
        new_basket_item.quantity = quantity
        new_basket_item.save()
    else:
        new_basket_item.delete()

    return render(request, 'basketapp/includes/inc_basket_list.html')
