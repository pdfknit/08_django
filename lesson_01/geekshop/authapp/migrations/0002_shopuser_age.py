# Generated by Django 4.0.1 on 2022-01-28 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopuser',
            name='age',
            field=models.PositiveIntegerField(blank=True, default=10, verbose_name='Возраст'),
            preserve_default=False,
        ),
    ]
