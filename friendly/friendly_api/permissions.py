from rest_framework import permissions


class IsResourceOwner(permissions.BasePermission):
    """
    Define permissions for resource owners
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class IsSelfOrFriend(permissions.BasePermission):


    def has_object_permission(self, request, view, obj):
        return True #TODO: lookup if person performing this is a friend