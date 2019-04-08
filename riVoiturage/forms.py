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
                '',
                'placeholder': ''
            }),
        required=True,
        initial='')
    telephone = forms.CharField(
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

    password1 = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(
            attrs={
                'class':
                '',
                'placeholder': ''
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
                '',
                'placeholder': ''
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
                '',
                'placeholder': ''
            }),
        required=True,
        initial='')
    nni = forms.IntegerField(
        label="Nni",
        widget=forms.TextInput(
            attrs={
                'class':
                '',
                'placeholder': ''
            }),
        required=True,
        initial=''
    )
    telephone = forms.CharField(
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
    permis = forms.IntegerField(
        label="Permis",
        widget=forms.TextInput(
            attrs={
                'class':
                '',
                'placeholder': ''
            }),
        required=True,
        initial=''
    )
    password1 = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(
            attrs={
                'class':
                '',
                'placeholder': ''
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
                '',
                'placeholder': ''
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
                'form-control g-color-black g-bg-white g-bg-white--focus g-brd-gray-light-v4 g-brd-primary--hover rounded g-py-15 g-px-15',
                'placeholder':
                ''
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
                'form-control g-color-black g-bg-white g-bg-white--focus g-brd-gray-light-v4 g-brd-primary--hover rounded g-py-15 g-px-15 mb-3',
                'placeholder':
                ''
            }),
        required=True
    )
