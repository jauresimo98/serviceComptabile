from django import forms
from .models import ReleveCompte

class ReleveCompteForm(forms.ModelForm):
    class Meta:
        model = ReleveCompte
        fields = ('numero', 'nomDestinataire', 'montant','date' ,'signataire1','signataire2','signataire3' )
