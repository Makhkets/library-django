from rest_framework.permissions import BasePermission

import loguru
from api.models import JWTokens


class ActionPermissionClassesMixin(object):
    def get_permissions(self):
        """
        Позволяет указать свои разрешения на каждое действие
        """
        if self.action_permission_classes and self.action in self.action_permission_classes:
            permissions = self.action_permission_classes[self.action]
            return [permission() for permission in permissions]
        return super(ActionPermissionClassesMixin, self).get_permissions()

class IsTokenAuth(BasePermission):
    def has_permission(self, request, view):
        try:
            jwt = JWTokens.objects.get(token=request.headers.get('Authorization').split("Benefix ")[1])
            jwt.count = int(jwt.count) - 1
            jwt.save()
            return True
        except: return False

class IsTokenAdminAuth(BasePermission):
    def has_permission(self, request, view):
        try:
            jwt = JWTokens.objects.get(token=request.headers.get('Authorization').split("Benefix ")[1])
            jwt.count = int(jwt.count) - 1
            jwt.save()
            if jwt.isAdmin:
                return True
            return False
        except: return False

class AlwaysNotAuth(BasePermission):
    def has_permission(self, request, view):
        return False
