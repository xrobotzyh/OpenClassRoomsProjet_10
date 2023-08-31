from rest_framework import permissions

from project.models import Contributor


# check the connected user is contributor of the project
def is_contributor(user_id, project_id) -> bool:
    return Contributor.objects.filter(user_id=user_id, project_id=project_id).exists()


class HasProjectPermissions(permissions.BasePermission):

    def has_object_permission(self, request, view, obj) -> bool:
        if view.action in {"list", "retrieve"}:
            return obj.author == request.user or obj.contributors.filter(user_id=request.user.id,
                                                                         project_id=view.kwargs["pk"]).exists()
        # for delete , put , update, create needs author permission
        if view.action in {"destroy", 'partial_update', "update", "create"}:
            return obj.author == request.user


class HasIssuePermissions(permissions.BasePermission):
    def has_permission(self, request, view) -> bool:
        return is_contributor(user_id=request.user.id, project_id=view.kwargs["project_id"])

    def has_object_permission(self, request, view, obj):
        if view.action in {'update', 'partial_update', 'destroy'}:
            return obj.author == request.user
        else:
            return True


class HasCommentPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        return is_contributor(user_id=request.user.id, project_id=view.kwargs["project_id"])

    def has_object_permission(self, request, view, obj):
        if view.action in {'update', 'partial_update', 'destroy'}:
            return obj.author == request.user
        else:
            return True
