
from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register("produit", ProduitViewset)
router.register("vente", VenteViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/',include('rest_framework.urls')),
]
