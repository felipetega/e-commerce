# Generated by Django 4.0.5 on 2022-12-30 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_rename_produto_img_produto_produto_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='produto_img',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
