# Generated by Django 4.2.4 on 2023-08-21 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_categoriey_remove_shop_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='categories',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop.categoriey'),
            preserve_default=False,
        ),
    ]