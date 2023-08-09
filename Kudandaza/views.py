from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import ProduitSerializer, VenteSerializer
from rest_framework.permissions import *

class ProduitViewset(viewsets.ModelViewSet):
    queryset = Produit.objects.all()
    permission_classes = IsAuthenticatedOrReadOnly,
    serializer_class = ProduitSerializer

class VenteViewset(viewsets.ModelViewSet):
    queryset = Vente.objects.all()
    permission_classes = IsAuthenticatedOrReadOnly,
    serializer_class = VenteSerializer

    def perform_create(self,serializer,):
        data = serializer.validated_data
        produit = data['produit']
        cout = data['quantite_vendu'] * produit.prix_de_vente_unitaire
        serializer.save(prix_de_vente_total=cout)
        serializer.save(umudandaza=self.request.user)
        return serializer


