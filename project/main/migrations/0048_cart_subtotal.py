# Generated by Django 4.0.5 on 2023-01-08 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0047_alter_cart_fee'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
    ]