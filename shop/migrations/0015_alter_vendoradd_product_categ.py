# Generated by Django 4.2.4 on 2023-09-01 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_vendoradd_product_categ'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendoradd',
            name='product_categ',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prod_categ', to='shop.categoriey'),
        ),
    ]
