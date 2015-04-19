from django import forms
from EMA.models import Eleve,Matiere,Notes

class Inscription(forms.ModelForm):
        no_Dossier = forms.IntegerField(label='Numero de dossier',max_length=20)
        compte = forms.CharField(label='Compte utilisateur',max_length=20)
        mot_de_passe =forms.CharField(label='mot de passe',widget=forms.PasswordInput() )
        nom = forms.CharField(label='NOM',max_length=20)
        prenom = forms.CharField(label='Prenom',max_length=20)
        email = forms.EmailField(label=u"Votre adresse mail",max_length=20)
        
