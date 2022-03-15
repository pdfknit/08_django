from django.db import models
from django.conf import settings

# Create your models here.
from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from mainapp.models import Product
from basketapp.models import Basket


class Order(models.Model):
    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'
        ordering = ('-created',)

    ORDER_STATUS_CHOICES = (
        ('in_process', 'в обработке'),
        ('created', 'создан'),
        ('canceled', 'отменен'),
        ('paid', 'оплачен'),
        ('ready', 'готов к выдаче'),
        ('received', 'получен'),
        ('awaiting payment', 'ждет оплаты'),

    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(verbose_name='создан', auto_now_add=True)
    updates = models.DateTimeField(verbose_name='обновлен', auto_now=True)
    status = models.CharField(verbose_name="статус заказа", choices=ORDER_STATUS_CHOICES, max_length=20, default='created')
    is_active = models.BooleanField(verbose_name='активен', default=True)

    @property
    def items_with_products(self):
        return self.items.select_related('product')
    def ___str__(self):
        return f'Заказ {self.id}\nСтатус заказа:{self.status}'

    def get_total_cost(self):
        return sum(item.cost for item in self.items_with_products)

    def get_total_quantity(self):
        return sum(item.quantity for item in self.items.all())

    def delete(self):
        for item in self.items_with_products:
            try:
                Basket.objects.create(user=self.user, product=item.product, quantity=item.quantity)
            except:
                pass
        self.is_active = False
        self.status = 'canceled'
        self.save()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)

    @property
    def cost(self):
        return self.product.price * self.quantity

@receiver(pre_save, sender=OrderItem)
def update_quantity_on_save(sender, update_fields, instance, **kwargs):
    if instance.pk:
        old_item = OrderItem.objects.get(pk=instance.pk)
        instance.product.quantity -= instance.quantity - old_item.quantity
    else:
        instance.product.quantity -= instance.quantity
        pass
    instance.product.save()

@receiver(pre_delete, sender=OrderItem)
def update_quantity_on_delete(sender, instance, **kwargs):
    instance.product.quantity += instance.quantity
    instance.product.save()