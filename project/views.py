from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from authentification.models import UserProfile
from .models import Project, Contributor
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user_instance = self.request.user
        project_instance = serializer.save(author=user_instance)
        Contributor.objects.create(user=user_instance, project=project_instance)
