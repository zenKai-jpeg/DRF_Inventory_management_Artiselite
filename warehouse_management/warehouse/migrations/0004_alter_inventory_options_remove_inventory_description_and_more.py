# Generated by Django 5.1 on 2024-09-03 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0003_inbound_reference_inbound_remarks_outbound_reference_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inventory',
            options={'verbose_name_plural': 'inventories'},
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='description',
        ),
        migrations.AddField(
            model_name='inbound',
            name='location',
            field=models.CharField(choices=[('A', 'Storage A'), ('B', 'Storage B'), ('C', 'Storage C'), ('D', 'Storage D')], default='A', max_length=1),
        ),
        migrations.AlterField(
            model_name='inbound',
            name='remarks',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='product_sku',
            field=models.CharField(editable=False, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='outbound',
            name='remarks',
            field=models.TextField(),
        ),
    ]
