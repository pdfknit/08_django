from django.urls import path, re_path
import authapp.views as authapp
from django.conf.urls import include
from . import views

app_name = 'authapp'

urlpatterns = [
    path('login/', authapp.login, name='login'),
    path('logout/', authapp.logout, name='logout'),
    path('register/', authapp.register, name='register'),
    path('edit/', authapp.edit, name='edit'),
    re_path(r'^verify/(?P<email>.+)/(?P<activation_key>\w+)/$', views.verify, name='verify')
]