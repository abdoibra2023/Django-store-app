# Generated by Django 4.2.4 on 2023-08-30 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_shop_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='vendor_name',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]