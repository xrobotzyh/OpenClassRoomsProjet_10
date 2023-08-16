from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'inscription', viewset=views.UserInscriptionViewSet, basename='userinscription')

# urlpatterns = [
    # path('inscription/', UserInscriptionView.as_view()),
# 
# ]
