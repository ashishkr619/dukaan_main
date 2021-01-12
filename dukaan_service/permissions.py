from django.conf import settings
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions


class AllowAuthenticatedRead(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            if request.user.is_anonymous:
                return False
        return True


class AllowOptionsAuthentication(IsAuthenticated):
    def has_permission(self, request, view):
        if request.method == 'OPTIONS':
            return True

        if getattr(request, 'session', None) and \
                request.session.get('jwt_iss') == settings.JWT_ALLOWED_ISSUER:
            return True

        return request.user and request.user.is_authenticated
