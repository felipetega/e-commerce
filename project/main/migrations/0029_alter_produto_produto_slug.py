# Generated by Django 4.0.5 on 2022-12-30 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_produto_produto_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='produto_slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
