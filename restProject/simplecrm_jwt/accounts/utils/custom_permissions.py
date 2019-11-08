from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.account.owner == request.user