from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from authapp.models import ShopUser
from adminapp.utils import superuser_required_decorator
from adminapp.forms import ShopUserAdminForm
from django.urls import reverse

from authapp.forms import ShopUserRegisterForm


@superuser_required_decorator
def user_create(request):
    title = 'пользователи/создание'

    if request.method == 'POST':
        user_form = ShopUserRegisterForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('admin:users'))
    else:
        user_form = ShopUserRegisterForm()

    content = {'title': title, 'update_form': user_form}

    return render(request, 'adminapp/user_edit.html', content)


@superuser_required_decorator
def users(request):
    users = ShopUser.objects.all().order_by('id')

    return render(request, 'adminapp/users.html', context={
        'title': 'Пользователи',
        'objects': users,
    })

@superuser_required_decorator
def user_edit(request, pk):
    title = 'пользователи/редактирование'

    edit_user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        edit_form = ShopUserAdminForm(request.POST, request.FILES, instance=edit_user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:user_edit', args=[edit_user.pk]))
    else:
        edit_form = ShopUserAdminForm(instance=edit_user)

    content = {'title': title, 'update_form': edit_form}

    return render(request, 'adminapp/user_edit.html', content)


@superuser_required_decorator
def user_delete(request, pk):
    title = 'Удалить пользователя'

    user = get_object_or_404(ShopUser, pk=pk)

    if request.method == 'POST':
        # user.delete()
        # вместо удаления лучше сделаем неактивным
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('admin:users'))

    content = {'title': title, 'user_to_delete': user}

    return render(request, 'adminapp/user/delete.html', content)

