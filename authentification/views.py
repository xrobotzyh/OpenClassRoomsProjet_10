from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from .models import UserProfile
from .permissions import HasUserprofilePermissions
from .serializers import UserInscriptionSerializer, UserSerializer


class UserInscriptionViewSet(CreateModelMixin, viewsets.GenericViewSet):
    # give the queryset and serializer
    queryset = UserProfile.objects.all()
    serializer_class = UserInscriptionSerializer


class UserManagementViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, HasUserprofilePermissions)
    pagination_class = PageNumberPagination
