# Generated by Django 5.0.1 on 2024-03-21 06:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothingsite', '0009_size_alter_product_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='clothingsite.size'),
        ),
    ]
