from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from mainapp.models import ProductCategory
from adminapp.forms import ProductCategoryAdminForm
from django.http.response import HttpResponseRedirect


def category_create(request):
    title = 'Создание категории'
    form = ProductCategoryAdminForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:categories'))
    else:
        user_form = ProductCategoryAdminForm()

    content = {'title': title, 'update_form': form,}

    return render(request, 'adminapp/category_edit.html', content)


def categories(request):
    categories = ProductCategory.objects.all().order_by('id')

    return render(request, 'adminapp/categories.html', context={
        'title': 'Пользователи',
        'objects': categories,
    })


def category_update(request, pk):
    category = get_object_or_404(ProductCategory, pk=pk)
    title = 'Изменить категорию'
    form = ProductCategoryAdminForm(request.POST, instance=category)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:categories'))
    else:
        user_form = ProductCategoryAdminForm(instance=category)

    content = {'title': title, 'update_form': form, }

    return render(request, 'adminapp/category_edit.html', content)


def category_delete(request, pk):
    title = 'пользователи/удаление'

    category = get_object_or_404(ProductCategory, pk=pk)

    if request.method == 'POST':
        # user.delete()
        # вместо удаления лучше сделаем неактивным
        category.is_active = False
        category.save()
        return HttpResponseRedirect(reverse('admin:users'))

    content = {'title': title, 'category_to_delete': category}

    return render(request, 'adminapp/category_delete.html', content)
