# Generated by Django 3.2.25 on 2025-03-28 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
