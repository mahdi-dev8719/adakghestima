# Generated by Django 4.1.7 on 2023-02-28 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0004_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='position',
            field=models.IntegerField(unique=True, verbose_name='شمارش'),
        ),
    ]
