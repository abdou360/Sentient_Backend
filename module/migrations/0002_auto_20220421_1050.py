# Generated by Django 3.0.7 on 2022-04-21 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('module', '0001_initial'),
        ('semestre', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='semestre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='semestre.Semestre'),
        ),
        migrations.AddField(
            model_name='enseignant_responsable',
            name='element_module',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='module.ElementModule'),
        ),
    ]
