# Generated by Django 4.0.5 on 2023-01-14 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0066_alter_creditcard_card_number_alter_creditcard_cvv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='number',
            field=models.CharField(max_length=50),
        ),
    ]
