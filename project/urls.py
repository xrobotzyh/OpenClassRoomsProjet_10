from rest_framework.routers import DefaultRouter

from . import views
from .views import ProjectViewSet, IssueViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'projects/(?P<project_id>\d+)/issues', IssueViewSet, basename='project-issues')
router.register(r'projects/(?P<project_id>\d+)/issues/(?P<issue_id>\d+)/comments', CommentViewSet, basename='issue-comments')
# router.register(r'projects/(?P<project_id>\d+)/contributors', ContributorViewSet, basename='project-contributors')
