# Generated by Django 4.0.5 on 2022-12-29 00:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_produto_produto_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='cliente_id',
            field=models.ForeignKey(default='', editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
