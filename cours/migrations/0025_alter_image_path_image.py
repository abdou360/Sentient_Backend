# Generated by Django 3.2.6 on 2022-04-28 04:11

import cours.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cours', '0024_alter_traitement_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='path_image',
            field=models.FileField(default='NULL', upload_to=cours.models.model_image_location),
        ),
    ]
