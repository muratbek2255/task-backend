# Generated by Django 4.0.4 on 2022-04-26 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_products_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.DecimalField(decimal_places=2, default=20.0, max_digits=7),
        ),
    ]
