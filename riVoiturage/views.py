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


@login_required(login_url='connexion')
def dashChauffeur(request):
    form=CreerTrajet(request.POST or None)
    fromVoiture = AjouterVoiture(request.POST or None)
    chauffeur= Chauffeur.objects.get(user=request.user)
    myTgs = Traget.objects.filter(chauffeur=chauffeur)

    if request.method == 'POST':
            if "create_tg" in request.POST:
                if form.is_valid():
                    try:
                        if chauffeur.voiture == None:
                            messages.add_message(
                                request, messages.ERROR,"Vous n'avez pas une voiture Merci d'ajouter votre voiture")
                            return render(request, 'RiVoiturage/dashChauffeur.htm', locals()) 
                        tg = Traget(
                            point_depart=form.cleaned_data['point_depart'],
                            point_arrive=form.cleaned_data['point_darrive'],
                            chauffeur=chauffeur,
                            prix = form.cleaned_data['prix'],
                            nbplace=form.cleaned_data['nbplace']
                        )
                        tg.save()
                        messages.add_message(
                                request, messages.ERROR,"Traget Creer avec succe !")
                        return render(request, 'RiVoiturage/dashChauffeur.htm', locals())
                    except Exception:
                        messages.add_message(
                                request, messages.ERROR,"Il n'exist pas un chauffeur avec ce numero")

            if  "add_car" in request.POST:
                if fromVoiture.is_valid():
                    try:
                        vr = Voiture(
                            marque=fromVoiture.cleaned_data['marque'],
                            matricule=fromVoiture.cleaned_data['matricule'],
                            carburant = fromVoiture.cleaned_data['carburant'],
                            capacite = fromVoiture.cleaned_data['capacite']
                        )  
                        vr.save()
                        chauffeur.voiture=vr
                        chauffeur.save()
                        messages.add_message(
                                    request, messages.SUCCESS,"Voiture ajouter avec success")
                    except Exception:
                        messages.add_message(
                                    request, messages.SUCCESS,"Inpossible d'ajouter la voiture")


    return render(request, 'RiVoiturage/dashChauffeur.htm', locals()) 

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
                    return redirect(reverse('dashClient'))
                except Client.DoesNotExist:
                    try:
                        chauffeur = Chauffeur.objects.get(user=user)
                        login(request, user)
                        return redirect(reverse('dashChauffeur'))
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
            chauffeur = Chauffeur(
                user=user,
                nni=form.cleaned_data['nni'],
                permis=form.cleaned_data['permis']
            )
            chauffeur.save()
            return redirect(reverse('dashChauffeur'))
    return render(request, 'RiVoiturage/compte_chauffeur.html', locals())    


@login_required(login_url='connexion')
def CreateTarget(request):
    form=CreerTrajet(request.POST or None)
    if form.is_valid():
            user = User.objects.get(username=form.cleaned_data['chauffeur'])
            chauffeur= Chauffeur.objects.get(user=user)
            if chauffeur.voiture == None:
                return  HttpResponse("Vous n'avez pas une voitures Merci d'ajouter votre voiture")
            tg = Traget(
                   point_depart=form.cleaned_data['point_depart'],
                   point_arrive=form.cleaned_data['point_darrive'],
                   prix=form.cleaned_data['prix'],
                   chauffeur=chauffeur,
                   nbplace = form.cleaned_data['nbplace']
                )
            tg.save()
            return redirect(reverse('dashClient'))
        # try:
        #     user = User.objects.get(username=form.cleaned_data['chauffeur'])
        #     chauffeur= Chauffeur.objects.get(user=user)
        #     if chauffeur.voiture == None:
        #         return  HttpResponse("Vous n'avez pas une voitures Merci d'ajouter votre voiture")
        #     tg = Traget(
        #            point_depart=form.cleaned_data['point_depart'],
        #            point_arrive=form.cleaned_data['point_darrive'],
        #            prix=form.cleaned_data['prix'],
        #            chauffeur=chauffeur
        #         )
        #     tg.save()
        #     return redirect(reverse('dashClient'))
        # except Exception:
        #      return  HttpResponse("Il n'exist pas un chauffeur avec ce numero")
    return render(request, 'RiVoiturage/CreateTarget.html', locals())

@login_required(login_url='connexion')
def Targets(request):
    targets=models.Traget.objects.all()
    context={
        'targets':targets
    }
    return render(request,'RiVoiturage/listeTraget.html',context)

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
    client = Client.objects.get(user=request.user)
    print(client.id)
    try:
        
        tg.client_set.get(pk=client.pk)
        messages.add_message(request, messages.INFO, "Reservation effectuer déja !? ")
        return redirect(reverse('dashClient'))
    except Client.DoesNotExist as identifier:
            if len(tg.client_set.all()) <= tg.nbplace  :
              
                tg.client_set.add(client)
                tg.nbplace = tg.nbplace - 1
                if tg.nbplace == 0:
                    tg.iscompleted = True
                tg.save()
                msg = "Reservsation passer avec success  "
                messages.add_message(request, messages.INFO, msg)
                return redirect(reverse('dashClient'))
            else:
        
                messages.add_message(request, messages.INFO, "Désolée le nombre de place reservé pour sont fini !")
                return redirect(reverse('dashClient'))
    return redirect(reverse('dashClient'))