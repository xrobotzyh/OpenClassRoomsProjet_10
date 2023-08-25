from rest_framework import permissions


class HasProjectPermissions(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if view.action in ("list", "retrieve"):
            print(view.kwargs["pk"])
            return obj.author == request.user or obj.contributors.filter(user_id=request.user.id,
                                                                         project_id=view.kwargs["pk"]).exists()

        if view.action in ("destroy", 'partial_update', "update", "create"):
            return obj.author == request.user


class HasIssuePermissions(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if view.action in ('retrieve', 'list', 'create'):
            return obj.author == request.user or obj.project.contributors.filter(user_id=request.user.id,
                                                                                 project_id=view.kwargs["pk"]).exists()
        elif view.action in ('update', 'partial_update', 'destroy'):
            return obj.author == request.user


class HasCommentPermissions(permissions.BasePermission, HasIssuePermissions):
    def has_object_permission(self, request, view, obj):
        if view.action in ('retrieve', 'list', 'create'):
            return obj.author == request.user or obj.project.contributors.filter(user_id=request.user.id,
                                                                                 project_id=view.kwargs["pk"]).exists()
        elif view.action in ('update', 'partial_update', 'destroy'):
            return obj.author == request.user

