# Generated by Django 3.0.7 on 2020-11-14 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0003_auto_20201114_2333'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='height',
            field=models.IntegerField(default=0, verbose_name='Height points'),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='width',
            field=models.IntegerField(default=0, verbose_name='Width points'),
        ),
    ]
