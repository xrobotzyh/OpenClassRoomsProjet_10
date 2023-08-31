from rest_framework import viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Project, Contributor, Issue, Comment
from .permissions import HasCommentPermissions, HasIssuePermissions, HasProjectPermissions
from .serializers import ProjectSerializer, IssueSerializer, CommentSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated, HasProjectPermissions)
    pagination_class = PageNumberPagination

    # save the connected user as author of the project he has just created automatic
    def perform_create(self, serializer):
        user_instance = self.request.user
        project_instance = serializer.save(author=user_instance)
        Contributor.objects.create(user=user_instance, project=project_instance)


class IssueViewSet(viewsets.ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = (IsAuthenticated, HasIssuePermissions)
    pagination_class = PageNumberPagination

    def get_queryset(self):
        project_id = self.kwargs.get('project_id')
        return Issue.objects.filter(project_id=project_id)

    #
    def perform_create(self, serializer):
        project_id = self.kwargs.get('project_id')
        project_instance = Project.objects.get(pk=project_id)
        # to check if the issuer creator is the contributor of the project, is not, no permission to do that
        if not project_instance.contributors.filter(user_id=self.request.user.id).exists():
            return Response({'detail': 'You are not a contributor of this project.'}, status=status.HTTP_403_FORBIDDEN)

        else:
            serializer.save(author=self.request.user, project=project_instance)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, HasCommentPermissions)
    pagination_class = PageNumberPagination

    def get_queryset(self):
        issue_id = self.kwargs.get('issue_id')
        project_id = self.kwargs.get('project_id')

        return Comment.objects.filter(issue_id=issue_id, project_id=project_id)

    def perform_create(self, serializer):
        project_id = self.kwargs.get('project_id')
        issue_id = self.kwargs.get('issue_id')
        project = Project.objects.get(id=project_id)
        issue = Issue.objects.get(project=project, id=issue_id)

        serializer.save(author=self.request.user, issue=issue, project=project)
