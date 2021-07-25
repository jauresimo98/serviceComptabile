from django.db import models
class Utilisateur (models.Model):
    TYPE_UTILISATEUR = (
        ('S', 'Secrétaire'),
        ('C', 'Chef Comptable'),
        ('A', 'Administrateur'),)
    login =  models.CharField(max_length=254, null=True)
    type_utilisateur = models.CharField(max_length=1, choices=TYPE_UTILISATEUR)
    password = models.CharField(max_length=255,null= True)
    
# Create your models here.
