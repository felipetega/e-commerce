# Generated by Django 4.0.5 on 2022-12-29 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_produto_produto_quantidade'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venda',
            old_name='produto_id',
            new_name='produto_nome',
        ),
    ]
