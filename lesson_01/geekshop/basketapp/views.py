from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from basketapp.models import Basket
from mainapp.models import Product
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import JsonResponse

@login_required()
def basket(request):
    content = {}
    return render(request, 'basketapp/basket.html', context={
        'basket': Basket.objects.filter(user=request.user),
        'title': 'Корзина',
    })


def add(request, pk):
    product = get_object_or_404(Product, pk=pk)

    basket = Basket.objects.filter(user=request.user, product=product).first()

    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def remove(request, pk):
    basket = get_object_or_404(Product, pk=pk)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def edit(request, pk, quantity):

    new_basket_item = Basket.objects.get(pk=pk)

    if quantity > 0:
        new_basket_item.quantity = quantity
        new_basket_item.save()
    else:
        new_basket_item.delete()

    return render(request, 'basketapp/includes/inc_basket_list.html')

