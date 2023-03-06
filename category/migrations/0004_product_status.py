# Generated by Django 4.1.7 on 2023-02-28 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.BooleanField(choices=[('d', 'پیش نویس'), ('p', 'منتشر شده')], default=True, verbose_name='نمایش؟'),
        ),
    ]
