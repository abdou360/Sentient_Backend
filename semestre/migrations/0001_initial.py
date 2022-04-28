# Generated by Django 4.0.3 on 2022-04-28 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('filiere', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Niveau',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_niveau', models.CharField(max_length=100, null=True)),
                ('type_niveau', models.CharField(max_length=100, null=True)),
                ('filiere', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='filiere.filiere')),
            ],
        ),
        migrations.CreateModel(
            name='Semestre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle_semestre', models.CharField(max_length=100, null=True)),
                ('niveau', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='semestre.niveau')),
            ],
        ),
        migrations.CreateModel(
            name='Groupe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_group', models.CharField(max_length=100, null=True)),
                ('niveau', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='semestre.niveau')),
            ],
        ),
        migrations.CreateModel(
            name='AnneUniversitaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=100, null=True)),
                ('date', models.DateField()),
                ('etudiant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.students')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='semestre.groupe')),
            ],
        ),
    ]
