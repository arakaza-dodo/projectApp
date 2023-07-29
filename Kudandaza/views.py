from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import ProduitSerializer, VenteSerializer

class ProduitViewset(viewsets.ModelViewSet):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer

class VenteViewset(viewsets.ModelViewSet):
    queryset = Vente.objects.all()
    serializer_class = VenteSerializer

def perform_create(self,serializer):
    data = serializer.validated_data
    produit = data['produit']
    cout = data['quantite_vendu'] 
    p=produit.prix_de_vente_unitaire
    serializer.save(prix_de_vente_total=cout* p)
    return serializer

    # def perform_create(self, serializer):
    #   serializer.save(uwayimuhaye=self.request.user)
    #   return serializer


