from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class ShopUser(AbstractUser):
    age = models.PositiveIntegerField(verbose_name="Возраст", blank=True)
    avatar = models.ImageField(verbose_name="Аватар", upload_to="avatars", blank=True)
    phone = models.CharField(verbose_name="Телефон", max_length=11, blank=True)