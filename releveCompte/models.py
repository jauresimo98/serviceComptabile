from django.db import models

class ReleveCompte (models.Model):
    numero = models.IntegerField(null=True,blank=True)
    nomDestinataire =  models.CharField(max_length=254, null=True)
    montant = models.IntegerField(blank=True, null=True)  # Field name made lowercase.                                   
    date = models.DateTimeField()  # Field name made lowercase.
    signataire1 =  models.CharField(max_length=254, null=True)
    signataire2 =  models.CharField(max_length=254, null=True)
    signataire3 =  models.CharField(max_length=254, null=True)

class Image(models.Model):
    
    image = models.ImageField(upload_to = 'static/images/')

# Create your models here.
