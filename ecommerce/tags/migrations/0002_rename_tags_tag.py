# Generated by Django 4.1.3 on 2022-12-04 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_product_featured'),
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tags',
            new_name='Tag',
        ),
    ]
