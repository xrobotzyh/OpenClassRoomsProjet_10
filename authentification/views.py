from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin

from .models import UserProfile
from .serializers import UserInscriptionSerializer, UserSerializer


class UserInscriptionViewSet(CreateModelMixin, viewsets.GenericViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserInscriptionSerializer

    # def post(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     user = serializer.save()
    #
    #     return Response({"token": token}, status=status.HTTP_201_CREATED)


class UserManagementViewSet(UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin, viewsets.GenericViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
