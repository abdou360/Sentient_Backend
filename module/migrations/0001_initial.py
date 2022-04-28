# Generated by Django 4.0.3 on 2022-04-28 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('semestre', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElementModule',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('libelle_element_module', models.CharField(max_length=200, null=True)),
                ('volumeHoraire', models.IntegerField()),
                ('objectif', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Perequis',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('element_module_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_element_module', to='module.elementmodule')),
                ('prerequis_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_prerequis', to='module.elementmodule')),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('libelle_module', models.CharField(max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('semestre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='semestre.semestre')),
            ],
        ),
        migrations.AddField(
            model_name='elementmodule',
            name='module',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='module.module'),
        ),
        migrations.AddField(
            model_name='elementmodule',
            name='prof_id',
            field=models.ManyToManyField(to='users.professeur'),
        ),
        migrations.AddField(
            model_name='elementmodule',
            name='responsable',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_responsable', to='users.professeur'),
        ),
    ]
