# Generated by Django 4.0.5 on 2022-12-29 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_venda_cliente_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='venda_id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
