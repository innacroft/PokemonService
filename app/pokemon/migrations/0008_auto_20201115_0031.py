# Generated by Django 3.0.7 on 2020-11-15 00:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0007_auto_20201115_0028'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemon',
            old_name='width',
            new_name='weight',
        ),
    ]