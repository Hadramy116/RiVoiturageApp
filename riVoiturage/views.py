from django.shortcuts import render
from django.http import HttpResponse
from .forms import NouveauCompte, CompteChauffeur, ConnexionForm
from .models import Client, Chauffeur
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'RiVoiturage/Home.html', locals()) 


def dash(request):
    return render(request, 'RiVoiturage/dashboard.html', locals()) 


def connexion(request):
    if request.user.is_authenticated:
        redirect(reverse('home'))
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)

            if user is not None:
                try:
                    client = Client.objects.get(user=user)
                    login(request, user)
                    isclient = "oui"
                    return redirect(reverse('home'))
                except Client.DoesNotExist:
                    try:
                        chauffeur = Chauffeur.objects.get(user=user)
                        login(request, user)
                        isclient = "Non"
                        return redirect(reverse('home'))
                    except Chauffeur.DoesNotExist:
                        messages.add_message(
                                    request, messages.ERROR,
                                    "Utilisateur inconnu ou mauvais de mot de passe !"
                                )
            else:
                messages.add_message(
                    request, messages.ERROR,
                    "Utilisateur inconnu ou mauvais de mot de passe !")
        else:
            messages.add_message(
                request, messages.ERROR,
                "Utilisateur inconnu ou mauvais de mot de passe !"
            )
    else:
        form = ConnexionForm()
    return render(request, 'RiVoiturage/connexion.html', locals())


def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))



def compte_client(request):
    form = NouveauCompte(request.POST or None)
    if form.is_valid():
  
        try:
            username = form.cleaned_data['telephone']
            User.objects.get(username=str(username))
            messages.error(request, 'Ce compte exite déjà !')
            return render(request, 'RiVoiturage/compte_client.html', locals())
        except User.DoesNotExist:
            user = User(
                    username=form.cleaned_data['telephone'],
                    first_name=form.cleaned_data['nom']
            )  
            user.set_password(form.cleaned_data['password1'])
            user.save()
            client = Client(user=user)
            client.save()
            return HttpResponse("Done")
    return render(request, 'RiVoiturage/compte_client.html', locals())    

def compte_chauffeur(request):
    form = CompteChauffeur(request.POST or None)
    if form.is_valid():
        try:
            username = form.cleaned_data['telephone']
            User.objects.get(username=str(username))
            messages.error(request, 'Ce compte exite déjà !')
            return render(request, 'RiVoiturage/compte_chauffeur.html', locals())
        except User.DoesNotExist:
            user = User(
                    username=form.cleaned_data['telephone'],
                    first_name=form.cleaned_data['nom']
            )  
            user.set_password(form.cleaned_data['password1'])
            user.save()
            chauffeur = Chauffeur(user=user)
            chauffeur.nni = form.cleaned_data['nni']
            chauffeur.permis = form.cleaned_data['permis']
            chauffeur.save()
            return HttpResponse("Done")
    return render(request, 'RiVoiturage/compte_chauffeur.html', locals())    