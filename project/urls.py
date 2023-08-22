from rest_framework.routers import DefaultRouter

from . import views

router_project = DefaultRouter()
router_project.register(r'projects', viewset=views.ProjectViewSet, basename='project')

router_issue = DefaultRouter()
router_issue.register(r'issues', viewset=views.IssueViewSet, basename='issues')

router_comment = DefaultRouter()
router_comment.register(r'comments', viewset=views.CommentViewSet, basename='comments')
