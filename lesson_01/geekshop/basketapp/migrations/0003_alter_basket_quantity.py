# Generated by Django 4.0.1 on 2022-03-05 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basketapp', '0002_alter_basket_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='количество'),
        ),
    ]
