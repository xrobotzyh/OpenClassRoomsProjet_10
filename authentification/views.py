from rest_framework import generics, status, viewsets
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response

# from rest_framework.response import Response
# from rest_framework_simplejwt.tokens import RefreshToken

from .models import UserProfile
from .serializers import UserInscriptionSerializer


class UserInscriptionViewSet(CreateModelMixin, viewsets.GenericViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserInscriptionSerializer

    # def post(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     user = serializer.save()
    #
    #     refresh = RefreshToken.for_user(user)
    #     token = str(refresh.access_token)
    #
    #     return Response({"token": token}, status=status.HTTP_201_CREATED)


class UserManagementViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserInscriptionSerializer

