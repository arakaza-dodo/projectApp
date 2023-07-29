from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Produit(models.Model):
    nom = models.CharField(max_length=100)
    prix_de_vente_unitaire = models.IntegerField(max_length=100)

    def __str__(self):
        return self.nom
    
class Vente(models.Model):
    produit = models.ForeignKey(Produit ,null=False ,on_delete=models.PROTECT)
    quantite_vendu = models.PositiveIntegerField(max_length=100) 
    prix_de_vente_total = models.FloatField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.PROTECT)


    # def save (self, *args, **kwargs):
    #     self.prix_de_vente_total = self.produit.prix_de_vente_unitaire * self.quantite_vendu
    #     super().save(*args, **kwargs)
    