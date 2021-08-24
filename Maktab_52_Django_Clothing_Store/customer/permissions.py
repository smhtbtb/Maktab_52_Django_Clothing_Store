from rest_framework import permissions


class IsSuperUser(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_superuser


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.phone == request.user.phone


class IsSuperUserOrOwner(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user or request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        return obj.phone == request.user.phone or request.user.is_superuser


class IsSuperUserOrOwnerAddress(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user or request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user or request.user.is_superuser
