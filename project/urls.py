from rest_framework.routers import DefaultRouter

from . import views

router_project = DefaultRouter()
router_project.register(r'project', viewset=views.ProjectViewSet, basename='project')
