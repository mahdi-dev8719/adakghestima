# Generated by Django 4.1.7 on 2023-02-28 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carcategory',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='motocategory',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='partscategory',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='vehiclescate',
            name='parent',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['position'], 'verbose_name': 'دسته بندی', 'verbose_name_plural': 'دسته بندی ها'},
        ),
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='title',
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='category',
            name='position',
            field=models.IntegerField(default=None, verbose_name='شمارش'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='status',
            field=models.BooleanField(default=True, verbose_name='نمایش؟'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, verbose_name='آدرس دسته بندی'),
        ),
        migrations.DeleteModel(
            name='BoatCategory',
        ),
        migrations.DeleteModel(
            name='CarCategory',
        ),
        migrations.DeleteModel(
            name='MotoCategory',
        ),
        migrations.DeleteModel(
            name='PartsCategory',
        ),
        migrations.DeleteModel(
            name='VehiclesCate',
        ),
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
    ]
