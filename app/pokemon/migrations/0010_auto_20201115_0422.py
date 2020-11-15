# Generated by Django 3.0.7 on 2020-11-15 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0009_auto_20201115_0235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='evolution',
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='evolution_graph',
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='order',
        ),
        migrations.AddField(
            model_name='evolution',
            name='evolves_to',
            field=models.IntegerField(default=0, verbose_name='ID next evolution'),
        ),
        migrations.AddField(
            model_name='evolution',
            name='id_chain',
            field=models.IntegerField(default=0, verbose_name='Evolution_chain'),
        ),
        migrations.AddField(
            model_name='evolution',
            name='pokemon_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='pokemon.Pokemon'),
        ),
        migrations.AlterField(
            model_name='evolution',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.CreateModel(
            name='Evolution_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_evolution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon.Evolution')),
            ],
        ),
    ]