from rest_framework import permissions


class HasUserprofilePermissions(permissions.BasePermission):

    # for endpoint of delete,update,put, need to see if the connected user is the requested
    def has_object_permission(self, request, view, obj) -> bool:
        if view.action in {"destroy", 'partial_update', "update"}:
            return obj.username == request.user.username
        else:
            return True
