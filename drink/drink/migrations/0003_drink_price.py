# Generated by Django 4.1.7 on 2023-03-22 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drink', '0002_drink_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='drink',
            name='price',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=15),
        ),
    ]