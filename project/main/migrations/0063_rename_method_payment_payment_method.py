# Generated by Django 4.0.5 on 2023-01-14 01:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0062_alter_cartitems_options_payment_cart_payment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='method',
            new_name='payment_method',
        ),
    ]
