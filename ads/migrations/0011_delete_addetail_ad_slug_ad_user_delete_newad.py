# Generated by Django 4.1.7 on 2023-03-04 00:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ads', '0010_alter_ad_cover'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AdDetail',
        ),
        migrations.AddField(
            model_name='ad',
            name='slug',
            field=models.SlugField(auto_created=True, default=None, unique=True, verbose_name='آدرس محصول'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ad',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='NewAd',
        ),
    ]
