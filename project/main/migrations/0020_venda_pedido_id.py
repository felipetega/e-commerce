# Generated by Django 4.0.5 on 2022-12-29 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_remove_venda_cliente_id_remove_venda_produtos'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda',
            name='pedido_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.pedido'),
            preserve_default=False,
        ),
    ]