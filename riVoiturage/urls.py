
from . import views
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('', views.home, name="home"),
    url(r'^compte_client$', views.compte_client, name="compte_client"),
    url(r'^compte_chauffeur$', views.compte_chauffeur, name="compte_chauffeur"),
    url(r'^connexion$', views.connexion, name='connexion'),
]