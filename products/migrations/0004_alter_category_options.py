# Generated by Django 3.2.25 on 2025-04-01 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_max_playing_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
