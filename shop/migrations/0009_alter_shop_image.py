# Generated by Django 4.2.4 on 2023-08-28 16:08

from django.db import migrations, models
import shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_alter_shop_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='image',
            field=models.ImageField(upload_to=shop.models.customize_image),
        ),
    ]
