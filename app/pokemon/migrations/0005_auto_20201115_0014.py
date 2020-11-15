# Generated by Django 3.0.7 on 2020-11-15 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0004_auto_20201114_2342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='height',
        ),
        migrations.AddField(
            model_name='pokemon',
            name='weight',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=19, verbose_name='Weight points'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='width',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=19, verbose_name='Width points'),
        ),
    ]