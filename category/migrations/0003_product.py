# Generated by Django 4.1.7 on 2023-02-28 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_remove_carcategory_parent_remove_motocategory_parent_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='دسته بندی محصول')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='آدرس دسته بندی')),
                ('category', models.ManyToManyField(to='category.category', verbose_name='دسته بندی')),
            ],
        ),
    ]
