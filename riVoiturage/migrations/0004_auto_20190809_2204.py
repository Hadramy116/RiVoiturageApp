# Generated by Django 2.1.7 on 2019-08-09 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riVoiturage', '0003_auto_20190809_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voiture',
            name='matricule',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
