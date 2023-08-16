from django.urls import path
from .views import UserInscriptionView

urlpatterns = [
    path('inscription/', UserInscriptionView.as_view()),
]