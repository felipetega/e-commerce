# Generated by Django 4.0.5 on 2023-01-06 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0043_alter_cart_ordered_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='ordered_products',
            field=models.ManyToManyField(blank=True, to='main.product'),
        ),
    ]
