# Generated by Django 3.2.6 on 2022-04-22 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cours', '0013_alter_modele3d_path'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='file',
            new_name='path',
        ),
        migrations.AlterField(
            model_name='modele3d',
            name='path',
            field=models.CharField(default='img/cours/modeles_3d/<django.db.models.fields.CharField>.2022-04-22-14-45-39', max_length=100),
        ),
    ]
