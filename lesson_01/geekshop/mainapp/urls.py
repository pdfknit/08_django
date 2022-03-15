from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.products, name='index'),
    path('<int:pk>', mainapp.category, name='category'),
    path('<int:pk>/<int:page>', mainapp.category, name='category_with_page'),
    path('product/<int:pk>/', mainapp.product, name='product'),
]