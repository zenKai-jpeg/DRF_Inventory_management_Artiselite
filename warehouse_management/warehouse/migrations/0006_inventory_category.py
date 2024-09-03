# Generated by Django 5.1 on 2024-09-03 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0005_inventory_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='category',
            field=models.CharField(choices=[('Electronic', 'Electronic'), ('Furniture', 'Furniture'), ('Clothing', 'Clothing')], default='Select a Category', max_length=50),
        ),
    ]
