# Generated by Django 4.0.5 on 2023-01-07 01:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0044_alter_cart_ordered_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='ordered_products',
        ),
    ]
