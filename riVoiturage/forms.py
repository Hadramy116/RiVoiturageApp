from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class NouveauCompte(forms.Form):
    nom = forms.CharField(
        label="Nom",
        max_length=40,
        widget=forms.TextInput(
            attrs={
                'class':
                'form-control',
                'placeholder': 'Nom'
            }),
        required=True,
        initial='')
    telephone = forms.CharField(
        label="Teléphone",
        widget=forms.TextInput(
            attrs={
                'class':
                'form-control',
                'placeholder': 'Teléphone'
            }),
        required=True,
        initial='',
        validators=[
            RegexValidator(
                regex=r'^\d{8}(?:\d{2})?$',
                message='Numero de téléphone incorrect')
        ])

    password1 = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(
            attrs={
                'class':
                'form-control',
                'placeholder': 'Mot de passe '
            }),
        required=True,
        validators=[
            RegexValidator(
                regex=r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$',
                message=
                'Votre mot de passe doit comprendre 8 caractères ou plus.')
        ])
    password2 = forms.CharField(
        label="Confirmation Mot de passe",
        widget=forms.PasswordInput(
            attrs={
                'class':
                'form-control',
                'placeholder': 'Confirmation Mot de passe'
            }),
        required=True,
        initial='',
        validators=[
            RegexValidator(
                regex= r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$',
                message=
                'Votre mot de passe doit comprendre 8 caractères ou plus.')
        ])

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                "Les deux mots de passe sont différents !")
            return password2


class CompteChauffeur(forms.Form):
    nom = forms.CharField(
        label="Nom",
        max_length=40,
        widget=forms.TextInput(
            attrs={
                'class':
                'form-control',
                'placeholder': 'Nom'
            }),
        required=True,
        initial='')
    nni = forms.IntegerField(
        label="Nni",
        widget=forms.TextInput(
            attrs={
                'class':
                'form-control',
                'placeholder': 'NNI'
            }),
        required=True,
        initial=''
    )
    telephone = forms.CharField(
        label="Teléphone",
        widget=forms.TextInput(
            attrs={
                'class':
                'form-control',
                'placeholder': 'Teléphone'
            }),
        required=True,
        initial='',
        validators=[
            RegexValidator(
                regex=r'^\d{8}(?:\d{2})?$',
                message='Numero de téléphone incorrect')
        ])
    permis = forms.IntegerField(
        label="Permis",
        widget=forms.TextInput(
            attrs={
                'class':
                'form-control',
                'placeholder': 'Permis'
            }),
        required=True,
        initial=''
    )
    password1 = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(
            attrs={
                'class':
                'form-control',
                'placeholder': 'Mot de passe'
            }),
        required=True,
        # validators=[
        #     RegexValidator(
        #         regex=r'^',
        #         message=
        #         'Votre mot de passe doit comprendre 8 caractères ou plus.')
        # ]
    )
    password2 = forms.CharField(
        label="Confirmation Mot de passe",
        widget=forms.PasswordInput(
            attrs={
                'class':
                'form-control',
                'placeholder': 'Confirmation Mot de passe'
            }),
        required=True,
        initial='',
        validators=[
            RegexValidator(
                regex= r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$',
                message=
                'Votre mot de passe doit comprendre 8 caractères ou plus.')
        ])

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                "Les deux mots de passe sont différents !")
            return password2



class ConnexionForm(forms.Form):
    username = forms.CharField(
        label="Téléphone",
        widget=forms.TextInput(
            attrs={
                'class':
                'form-control',
                'placeholder':
                'Téléphone'
            }),
        required=True,
        validators=[
            RegexValidator(
                regex=r'^\d{8}(?:\d{2})?$',
                message='Numero de téléphone incorrect')
        ])
    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(
            attrs={
                'class':
                'form-control',
                'placeholder':
                'Mot de passe'
            }),
        required=True
    )
    

class CreerTrajet(forms.Form):
    point_depart=forms.CharField(
        label="PointDepart",
        widget=forms.TextInput(attrs={
                'class':
                'form-control g-color-black g-bg-white g-bg-white--focus g-brd-gray-light-v4 g-brd-primary--hover rounded g-py-15 g-px-15',
                'placeholder':
                ''
            }),
        required=True,
    )
    point_darrive = forms.CharField(
        label="PointDarrive",
        widget=forms.TextInput(attrs={
            'class':
                'form-control g-color-black g-bg-white g-bg-white--focus g-brd-gray-light-v4 g-brd-primary--hover rounded g-py-15 g-px-15',
            'placeholder':
                ''
        }),
        required=True,
    )
    prix = forms.DecimalField(
        label="Prix",
        widget=forms.TextInput(attrs={
            'class':
                'form-control g-color-black g-bg-white g-bg-white--focus g-brd-gray-light-v4 g-brd-primary--hover rounded g-py-15 g-px-15',
            'placeholder':
                ''
        }),
        required=True,
    )
    # chauffeur = forms.CharField(
    #     label="Teléphone",
    #     widget=forms.TextInput(
    #         attrs={
    #             'class':
    #                 'form-control',
    #             'placeholder': ''
    #         }),
    #     required=True,
    #     initial='',
    #     validators=[
    #         RegexValidator(
    #             regex=r'^\d{8}(?:\d{2})?$',
    #             message='Numero de téléphone incorrect')
    #     ])


class AjouterVoiture(forms.Form):

    marque = forms.CharField(
        label="marque",
        widget=forms.TextInput(attrs={
            'class':
                'form-control g-color-black g-bg-white g-bg-white--focus g-brd-gray-light-v4 g-brd-primary--hover rounded g-py-15 g-px-15',
            'placeholder':
                ''
        }),
        required=True,
    )
    matricule=forms.CharField(
        label="matricule",
        widget=forms.TextInput(attrs={
            'class':
                'form-control g-color-black g-bg-white g-bg-white--focus g-brd-gray-light-v4 g-brd-primary--hover rounded g-py-15 g-px-15',
            'placeholder':
                ''
        }),

        required=True,
    )
    CARBURANT = (
        ('ESSENCE', 'ESSENCE'),
        ('GAZOILE', 'GAZOILE')
    )

    carburant = forms.ChoiceField(
        label="carburant",
        choices=CARBURANT,
        widget=forms.Select(attrs={
            'class':
                'form-control',
            'placeholder':
                ''
        }),
        
     
    )
    #     widget=forms.TextInput(attrs={
    #         'class':
    #             'form-control g-color-black g-bg-white g-bg-white--focus g-brd-gray-light-v4 g-brd-primary--hover rounded g-py-15 g-px-15',
    #         'placeholder':
    #             ''
    #     }),
    #
    #     required=True,
    # )
    capacite=forms.CharField(
        label="capacite",
        widget=forms.TextInput(attrs={
            'class':
                'form-control',
            'placeholder':
                ''
        }),

        required=True,
    )


class Reserver(forms.Form):
    client=forms.CharField(
        label="Teléphone",
        widget=forms.TextInput(
            attrs={
                'class':
                    '',
                'placeholder': ''
            }),
        required=True,
        initial='',
        validators=[
            RegexValidator(
                regex=r'^\d{8}(?:\d{2})?$',
                message='Numero de téléphone incorrect')
        ])

