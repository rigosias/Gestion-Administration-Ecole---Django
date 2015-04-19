from django.db import models

# Create your models here.
class Eleve(models.Model):
	id_Eleve = models.AutoField(primary_key=True)
	no_Dossier = models.IntegerField(max_length=20)
        compte = models.CharField(max_length=20,default='Entrer votre nom de compte')
        mot_de_passe = models.CharField(max_length=20,default='Entrer votre mot de passe')
	nom = models.CharField(max_length=20)
	prenom = models.CharField(max_length=20)
	email = models.EmailField(max_length=20)


	def __int__(self):
		return self.no_Dossier




class Matiere(models.Model):
	id_Matiere = models.AutoField(primary_key=True)
	nom_Matiere = models.CharField(max_length=100)
	coefficient = models.IntegerField()

	def __int__(self):
		return self.id_Matiere




class Notes(models.Model):
	id_Note = models.AutoField(primary_key=True)
	id_el_note = models.ForeignKey(Eleve)
	coef = models.ForeignKey(Matiere)
	note_Eleve = models.FloatField(max_length=5)

	def __int__(self):
		return self.id_Note



