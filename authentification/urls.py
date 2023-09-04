from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views
#register router
router_user = DefaultRouter()
router_user.register(r'inscription', viewset=views.UserInscriptionViewSet, basename='userinscription')
router_user.register(r'', viewset=views.UserManagementViewSet, basename='lists')
