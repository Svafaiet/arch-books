from rest_framework import permissions


class BookPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method == 'GET' or request.user.token.payload['type'] == 0

    def has_object_permission(self, request, view, obj):
        return request.method == 'GET' or request.user.token.payload['type'] == 0
