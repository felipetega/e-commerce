# Generated by Django 4.0.5 on 2022-12-29 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_venda_produtos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venda',
            name='produto_id',
        ),
    ]
