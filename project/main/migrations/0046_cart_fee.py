# Generated by Django 4.0.5 on 2023-01-08 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0045_remove_cart_ordered_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='fee',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
            preserve_default=False,
        ),
    ]
