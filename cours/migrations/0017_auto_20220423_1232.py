# Generated by Django 3.2.6 on 2022-04-23 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cours', '0016_auto_20220423_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modele3d',
            name='path',
            field=models.CharField(default='img/cours/modeles_3d/<django.db.models.fields.CharField>-2022-04-23-12-32-12', max_length=100),
        ),
        migrations.AlterField(
            model_name='traitement',
            name='label',
            field=models.CharField(max_length=100, null=True),
        ),
    ]