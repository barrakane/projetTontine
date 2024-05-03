from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class GroupeTontine(models.Model):
    nom = models.CharField(max_length=150)
    montantCotisation = models.CharField(max_length=150)
    frequencePaiment = models.CharField(max_length=150)
    dateCreation = models.DateTimeField(auto_now_add=True)
    dateDebut = models.DateTimeField(auto_now_add=True)
    dateFin = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f"{self.id}"
    

class Membre(models.Model):
    name = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    telephone = models.CharField(max_length=150)
    adress = models.CharField(max_length=150)
    group = models.ForeignKey(GroupeTontine, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name} - {self.prenom} - {self.telephone} - {self.adress}"
    
    
class Paiment(models.Model):
    montant = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    tour = models.CharField(max_length=150)
    membre = models.ForeignKey(Membre, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.montant} - {self.date} - {self.tour} "