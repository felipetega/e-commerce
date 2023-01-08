# Generated by Django 4.0.5 on 2023-01-04 19:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0038_alter_product_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0)),
                ('total_items', models.IntegerField(default=0)),
                ('quantity', models.IntegerField(default=1)),
            ],
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='cart_id',
            new_name='id',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='cart_total',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='cart_user',
        ),
        migrations.AddField(
            model_name='cart',
            name='total_price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
        migrations.AddField(
            model_name='cartitems',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.cart'),
        ),
        migrations.AddField(
            model_name='cartitems',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product'),
        ),
        migrations.AddField(
            model_name='cartitems',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
