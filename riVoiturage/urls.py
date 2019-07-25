
from . import views
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('', views.home, name="home"),
    url(r'^compte_client$', views.compte_client, name="compte_client"),
    url(r'^compte_chauffeur$', views.compte_chauffeur, name="compte_chauffeur"),
    url(r'^connexion$', views.connexion, name='connexion'),
    url(r'^deconnexion$', views.deconnexion, name='deconnexion'),

    url(r'^dashClient$', views.dash, name="dashClient"),
    url(r'^dashChauffeur$', views.dashChauffeur, name="dashChauffeur"),

     url(r'^createTraget$', views.CreateTarget, name='createTraget'),
    url(r'^ajouterVoiture$', views.Ajouter, name='ajouterVoiture'),
    url(r'^listeTraget$', views.Targets, name='listeTraget'),
    url('reserver/(?P<id>[0-9]+)/$',  views.Reserver, name='reserver'),

]