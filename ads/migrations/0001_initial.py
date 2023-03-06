# Generated by Django 4.1.7 on 2023-02-19 04:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='عنوان')),
                ('desc', models.TextField(max_length=1024, verbose_name='توضیحات')),
                ('cover', models.ImageField(upload_to='', verbose_name='عکس اصلی')),
                ('image', models.ImageField(upload_to='', verbose_name='عکس ها')),
                ('image_voice', models.ImageField(upload_to='', verbose_name='عکس و صوت')),
                ('video', models.FileField(upload_to='', verbose_name='فیلم')),
                ('voice', models.FileField(upload_to='', verbose_name='صوت')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='زمان انتشار')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='زمان بروزرسانی')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'آگهی',
                'verbose_name_plural': 'آگهی ها',
            },
        ),
        migrations.CreateModel(
            name='NewAd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='عنوان')),
                ('desc', models.TextField(max_length=1024, verbose_name='توضیحات')),
                ('cover', models.ImageField(upload_to='', verbose_name='عکس اصلی')),
                ('image', models.ImageField(upload_to='', verbose_name='عکس ها')),
                ('image_voice', models.ImageField(upload_to='', verbose_name='عکس و صوت')),
                ('video', models.FileField(upload_to='', verbose_name='فیلم')),
                ('voice', models.FileField(upload_to='', verbose_name='صوت')),
                ('state', models.CharField(max_length=20, verbose_name='استان')),
                ('city', models.CharField(max_length=20, verbose_name='شهر')),
                ('sell_type', models.CharField(max_length=20, verbose_name='نوع فروش')),
                ('brand', models.CharField(max_length=20, verbose_name='برند')),
                ('year', models.CharField(max_length=20, verbose_name='سال')),
                ('color', models.CharField(max_length=20, verbose_name='رنگ')),
                ('body', models.CharField(max_length=20, verbose_name='بدنه')),
                ('engine', models.CharField(max_length=20, verbose_name='موتور')),
                ('chassis', models.CharField(max_length=20, verbose_name='شاسی')),
                ('insurance', models.CharField(max_length=20, verbose_name='بیمه')),
                ('is_show', models.BooleanField(default=False, verbose_name='تایید آگهی')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='زمان انتشار')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='زمان بروزرسانی')),
                ('ads', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.ads')),
            ],
            options={
                'verbose_name': 'افزودن آگهی',
                'verbose_name_plural': 'آگهی های نو',
            },
        ),
    ]
