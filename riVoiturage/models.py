from django.db import models
from django.contrib.auth.models import User


class Chauffeur(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    nni = models.IntegerField()
    permis = models.CharField(max_length=16)
    adresse = models.CharField(max_length=20, blank=True, null=True)

class Voiture(models.Model):

    CARBURANT = (
        ('ESSENCE', 'ESSENCE'),
        ('GAZOILE', 'GAZOILE')
    )

    marque = models.CharField(max_length=10, blank=True, null=True)
    matricule = models.IntegerField()
    carburant = models.CharField(
        max_length=10,
        choices=CARBURANT,
        default='GAZOILE',
    )
    capacite = models.IntegerField()
    voiture = models.ForeignKey(Chauffeur, on_delete=models.CASCADE)



class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    adresse = models.CharField(max_length=20, blank=True, null=True)

    def __str__():
        return username


class Traget(models.Model):
    point_depart = models.CharField(max_length=10, blank=True, null=True)
    point_arrive = models.CharField(max_length=10, blank=True, null=True)
    clients = models.ForeignKey(Client, on_delete=models.CASCADE)
    Chauffeur = models.OneToOneField(
        Chauffeur,
        on_delete=models.CASCADE,
        primary_key=True,
    )