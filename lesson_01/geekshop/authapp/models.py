from datetime import timedelta
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now


# Create your models here.

def get_activation_key_expires():
    return now() + timedelta(days=2)


class ShopUser(AbstractUser):
    age = models.PositiveIntegerField(verbose_name="Возраст", blank=True, default=33)
    avatar = models.ImageField(verbose_name="Аватар", upload_to="avatars", blank=True)
    phone = models.CharField(verbose_name="Телефон", max_length=11, blank=True)
    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default=get_activation_key_expires)
