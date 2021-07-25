from import_export import resources
from .models import Personne
class PersonneResource(resources.ModelResource):
    class Meta:
        model = Personne