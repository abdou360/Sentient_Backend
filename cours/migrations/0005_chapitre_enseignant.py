# Generated by Django 3.2.6 on 2022-04-17 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_etudiant_professeur'),
        ('cours', '0004_auto_20220417_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapitre',
            name='enseignant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.professeur'),
            preserve_default=False,
        ),
    ]