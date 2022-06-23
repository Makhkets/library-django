from rest_framework.permissions import BasePermission

from loguru import logger as l
from api.models import JWTokens
from libraries.models import Book


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
            if jwt.count == 0:
                return False
            jwt.count = int(jwt.count) - 1
            jwt.save()
            return True
        except: return False

class IsTokenAdminAuth(BasePermission):
    def has_permission(self, request, view):
        try:
            jwt = JWTokens.objects.get(token=request.headers.get('Authorization').split("Benefix ")[1])
            if jwt.count == 0:
                return False
            jwt.count = jwt.count - 1
            jwt.save()
            if jwt.isAdmin:
                return True
            return False
        except: return False

class IsAuthorPostTokenAuth(BasePermission):
    def has_permission(self, request, view):
        try:
            jwt = JWTokens.objects.get(token=request.headers.get('Authorization').split("Benefix ")[1])
            if jwt.count == 0:
                return False
            jwt.count = jwt.count - 1
            jwt.save()
            if request.method in ["PATCH", "DELETE", "PUT"]:
                book_id = view.kwargs.get("pk")
                book = Book.objects.get(pk=book_id)
                if book.create_user.id == request.user.id:
                   return True
                else: return False
            return True
        except: return False

class AlwaysNotAuth(BasePermission):
    def has_permission(self, request, view):
        return False
