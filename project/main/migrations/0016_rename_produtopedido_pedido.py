# Generated by Django 4.0.5 on 2022-12-29 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_remove_venda_produto_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProdutoPedido',
            new_name='Pedido',
        ),
    ]
