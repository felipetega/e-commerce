# Generated by Django 4.0.5 on 2023-01-14 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0064_creditcard_alter_cart_payment_delete_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcard',
            name='card_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='cvv',
            field=models.IntegerField(),
        ),
    ]