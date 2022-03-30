from datetime import timedelta
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

def get_activation_key_expires():
    return now() + timedelta(days=2)


class ShopUser(AbstractUser):
    age = models.PositiveIntegerField(verbose_name="Возраст", blank=True, default=33)
    avatar = models.ImageField(verbose_name="Аватар", upload_to="avatars", blank=True)
    phone = models.CharField(verbose_name="Телефон", max_length=11, blank=True)
    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default=get_activation_key_expires)

class ShopUserProfile(models.Model):
    GENDER_CHOICES = (
        ('MALE', 'Мужской'),
        ('FEMALE', 'Женский'),
        ('NON_BINARY', 'Другой'),

    )
    user = models.OneToOneField(ShopUser, null=False, on_delete=models.CASCADE, db_index=True, related_name='profile')
    about = models.TextField(verbose_name="О себе", blank=True)
    gender = models.CharField(verbose_name="Гендер", choices=GENDER_CHOICES, max_length=10, blank=True)

@receiver(post_save, sender=ShopUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        ShopUserProfile.objects.create(user=instance)
    else:
        instance.profile.save()

