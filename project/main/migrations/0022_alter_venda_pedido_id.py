# Generated by Django 4.0.5 on 2022-12-30 14:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_rename_pedido_carrinho'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='pedido_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
