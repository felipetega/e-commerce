# Generated by Django 4.0.5 on 2023-01-14 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0065_alter_creditcard_card_number_alter_creditcard_cvv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcard',
            name='card_number',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='cvv',
            field=models.CharField(max_length=50),
        ),
    ]
