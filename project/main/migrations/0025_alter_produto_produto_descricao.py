# Generated by Django 4.0.5 on 2022-12-30 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_produto_produto_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='produto_descricao',
            field=models.TextField(default='Game'),
        ),
    ]
