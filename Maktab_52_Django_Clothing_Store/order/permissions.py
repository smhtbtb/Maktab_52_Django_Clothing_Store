from rest_framework import permissions


class IsSuperUser(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_superuser


class IsSuperUserOrOwner(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user or request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.is_superuser


class IsSuperUserOrOwnerItem(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user or request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        return obj.order.user == request.user or request.user.is_superuser
