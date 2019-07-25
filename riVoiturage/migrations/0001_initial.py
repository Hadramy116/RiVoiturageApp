# Generated by Django 2.1.7 on 2019-04-21 23:14

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chauffeur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nni', models.IntegerField()),
                ('permis', models.CharField(max_length=16)),
                ('adresse', models.CharField(blank=True, max_length=20, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adresse', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Traget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point_depart', models.CharField(blank=True, max_length=10, null=True)),
                ('point_arrive', models.CharField(blank=True, max_length=10, null=True)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('chauffeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='riVoiturage.Chauffeur')),
            ],
        ),
        migrations.CreateModel(
            name='Voiture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marque', models.CharField(blank=True, max_length=10, null=True)),
                ('matricule', models.IntegerField()),
                ('carburant', models.CharField(choices=[('ESSENCE', 'ESSENCE'), ('GAZOILE', 'GAZOILE')], default='GAZOILE', max_length=10, null=True)),
                ('capacite', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='traget',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='riVoiturage.Traget'),
        ),
        migrations.AddField(
            model_name='client',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='chauffeur',
            name='voiture',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='riVoiturage.Voiture'),
        ),
    ]
