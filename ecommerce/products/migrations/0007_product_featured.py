# Generated by Django 4.1.3 on 2022-12-04 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_timestamp_alter_product_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
