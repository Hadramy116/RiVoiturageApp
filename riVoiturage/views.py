from django.shortcuts import render
from django.http import HttpResponse
from .forms import NouveauCompte, CompteChauffeur, ConnexionForm, CreerTrajet, AjouterVoiture,Reserver
from .models import Client, Chauffeur,Traget,Voiture
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from riVoiturage import models


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def home(request):
    tragets = Traget.objects.all()
    return render(request, 'RiVoiturage/Home.html', locals()) 

@login_required(login_url='connexion')
def dash(request):
    targets=models.Traget.objects.all()
    return render(request, 'RiVoiturage/dashClient.html', locals()) 


def connexion(request):
    if request.user.is_authenticated:
       return redirect(reverse('home'))
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
                    return redirect(reverse('dashClient'))
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
    if request.user.is_authenticated:
       return redirect(reverse('home'))
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
            return redirect(reverse('dashClient'))
    return render(request, 'RiVoiturage/compte_client.html', locals())    

def compte_chauffeur(request):
    if request.user.is_authenticated:
       return redirect(reverse('home'))

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


@login_required(login_url='connexion')
def CreateTarget(request):
    form=CreerTrajet(request.POST or None)

    if form.is_valid():
        tg = Traget()
        tg.point_depart=form.cleaned_data['point_depart']
        tg.point_arrive=form.cleaned_data['point_darrive']
        try:
            user = User.objects.get(username=form.cleaned_data['chauffeur'])
            tg.chauffeur= Chauffeur.objects.get(user=user)
            tg.save()
        except Exception:
             return  HttpResponse("Il n'exist pas un chauffeur avec ce numero")
        return  HttpResponse("Success")
    return render(request, 'RiVoiturage/CreateTarget.html', locals())

@login_required(login_url='connexion')
def Targets(request):
    targets=models.Traget.objects.all()
    context={
        'targets':targets
    }
    return render(request,'RiVoiturage/listeTraget.html',context)


# def chouffeurs(request):
#     chouffrs=models.Chauffeur.objects.all()
#     context={
#         'chouffrs':chouffrs
#     }
#     return render(request,'ListeChouffeus.html',context)

@login_required(login_url='connexion')
def Ajouter(request):

    form=AjouterVoiture(request.POST or None)
    if form.is_valid():
        vr = Voiture()
        vr.marque=form.cleaned_data['marque']
        vr.matricule=form.cleaned_data['matricule']
        vr.carburant = form.cleaned_data['carburant']
        vr.capacite = form.cleaned_data['capacite']
        vr.save()
        # user = User.objects.get(username=form.cleaned_data['chauffeur'])
        # tg.chauffeur= Chauffeur.objects.get(user=user)
        # tg.save()
        return  HttpResponse("Success")
    return render(request, 'RiVoiturage/ajouterVoiture.html', locals())

@login_required(login_url='connexion')
def Reserver(request, id):
    tg = Traget.objects.get(pk=id)

    try:
        client = Client.objects.get(user=request.user)
        try :
            if tg.client_set.get(user=request.user):
                return HttpResponse("Reservation effectuer deja !? ")
        except Exception:
            if len(tg.client_set.all()) <= 5  :
                tg.client_set.add(client)
                tg.save()
                return HttpResponse("Reservsation passer avec success ")
            else:
                return HttpResponse("Chercher un autre traget")

    except Client.DoesNotExist:
        raise Http404("Client does not exist !!!")
        #HttpResponse("Client does not exist !!!")
    return render(request, 'RiVoditurage/reserver.html', tg)