from django.db import models
from django.utils.translation import gettext_lazy as gz


# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')
    description = models.TextField(max_length=128, verbose_name='Описание', blank=True)

    def __str__(self):
        return self.name


class ProductManager(models.Manager):
    def active_items(self):
        return Product.objects.filter(is_active=True)


class Product(models.Model):
    class ChoiceColor(models.TextChoices):
        NO = 'не указан', gz('не указан')
        BLACK = 'черный', gz('черный')
        RED = 'красный', gz('красный')
        BLUE = 'синий', gz('синий')
        YELLOW = 'желтый', gz('желтый')

    name = models.CharField(max_length=128, verbose_name='Имя')
    price = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена', default=0)
    image = models.ImageField(verbose_name='Изображение', blank=True, upload_to='products')
    description = models.CharField(max_length=128, verbose_name='Описание', blank=True)
    color = models.CharField(max_length=10, choices=ChoiceColor.choices, default=ChoiceColor.NO, verbose_name='Цвет')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    is_active = models.BooleanField(verbose_name='активный', default=True)

    objects = ProductManager()

    def __str__(self):
        return self.name
