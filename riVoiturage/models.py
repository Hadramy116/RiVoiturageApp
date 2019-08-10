from django.db import models
from datetime import datetime 
from django.contrib.auth.models import User


class Voiture(models.Model):

    CARBURANT = (
        ('ESSENCE', 'ESSENCE'),
        ('GAZOILE', 'GAZOILE')
    )

    marque = models.CharField(max_length=10, blank=True, null=True)
    matricule = models.CharField(max_length=10, blank=True, null=True)
    carburant = models.CharField(
        max_length=10,
        choices=CARBURANT,
        default='GAZOILE',
        null=True,
    )
    capacite = models.IntegerField()
   


class Chauffeur(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    nni = models.IntegerField()
    permis = models.CharField(max_length=16)
    adresse = models.CharField(max_length=20, blank=True, null=True)
    voiture=models.ForeignKey(Voiture, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.user.username


class Traget(models.Model):
    point_depart = models.CharField(max_length=10, blank=True, null=True)
    point_arrive = models.CharField(max_length=10, blank=True, null=True)
    chauffeur = models.ForeignKey(
        Chauffeur,
        on_delete=models.CASCADE
    )
    date=models.DateTimeField(default=datetime.now, blank=True)
    prix  = models.DecimalField( max_digits=19, decimal_places=0)
    nbplace = models.IntegerField()
    iscompleted = models.BooleanField(default=False)

    def __str__(self):
        return self.point_depart

    def get_clients(self):
        return self.client_set.all()


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    adresse = models.CharField(max_length=20, blank=True, null=True)
    traget = models.ForeignKey(Traget, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.user.username


