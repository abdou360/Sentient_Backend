# Generated by Django 3.2.6 on 2022-04-14 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cours', '0002_auto_20220414_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapitre',
            name='description',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
