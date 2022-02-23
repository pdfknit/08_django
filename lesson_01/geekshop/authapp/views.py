from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from authapp.forms import ShopUserLoginForm
from authapp.forms import ShopUserRegisterForm
from authapp.forms import  ShopUserEditForm
from .models import ShopUser
from django.contrib import auth
from django.urls import reverse
from .utils import send_verify_mail
from django.contrib import messages


def login(request):
    title = 'вход'

    if request.method == 'POST':
        login_form = ShopUserLoginForm(data=request.POST)
        if login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']


            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                if 'next' in request.GET.keys():
                    return HttpResponseRedirect(request.GET['next'])
                else:
                    return HttpResponseRedirect(reverse('main'))
    else:
        login_form = ShopUserLoginForm()
    content = {'title': title, 'login_form': login_form, }
    return render(request, 'authapp/login.html', content)


def register(request):
    title = 'регистрация'

    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            user = register_form.save()
            send_verify_mail(user)
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = ShopUserRegisterForm()

    content = {'title': title, 'register_form': register_form}

    return render(request, 'authapp/register.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))


def edit(request):
    title = 'редактирование'

    if request.method == 'POST':
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form = ShopUserEditForm(instance=request.user)

    content = {'title': title, 'edit_form': edit_form}

    return render(request, 'authapp/edit.html', content)

def verify(request, email, activation_key):
    user = get_object_or_404(ShopUser, email=email)
    if user.activation_key == activation_key:
        user.is_active = True
        user.save()
        auth.login(request, user)
    return render(request, 'authapp/verify.html')



