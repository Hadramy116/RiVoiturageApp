# Generated by Django 2.1.7 on 2019-08-09 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riVoiturage', '0004_auto_20190809_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traget',
            name='prix',
            field=models.DecimalField(decimal_places=0, max_digits=19),
        ),
    ]
