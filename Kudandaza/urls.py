
from django.urls import path, include
from rest_framework import routers
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register("produit", ProduitViewset)
router.register("vente", VenteViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('login/',TokenObtainPairView.as_view()),
    path('refresh/',TokenRefreshView.as_view()),
    path('api-auth/',include('rest_framework.urls')),
]
