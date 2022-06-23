from rest_framework import generics, viewsets
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated,\
                                                IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from api.searializers import BookSerializers, JWTSerializers

from libraries.models import Book, Category, User
from api.models import JWTokens
from api.exceptions import MissingTokenException
from api.permissions import ActionPermissionClassesMixin, IsTokenAuth,\
                            AlwaysNotAuth, IsTokenAdminAuth, IsAuthorPostTokenAuth

from loguru import logger as l
from pprint import pprint


# class BookAPIView(APIView):
#     def get(self, request):
#         books = Book.objects.all().values()
#         return Response({"books": list(books)})
#
#     def post(self, request):
#         new_book = Book.objects.create(
#             title=request.data['title'],
#             description=request.data['description'],
#             category=request.data['category'],Ы
#         )
#         return Response({"post": model_to_dict(new_book)})


# class BookAPIView(APIView):
#     def get(self, request):
#         books = Book.objects.all()
#         return Response({"posts": BookSerializers(books, many=True).data})
#
#     def post(self, request):
#         serializer = BookSerializers(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         # title = request.data.get("title")
#         # description = request.data.get("description")
#         # photo = request.data.get("photo")
#         # category = Category.objects.get(name=request.data.get("category"))
#         # user = User.objects.get(username=request.data.get("user"))
#
#         # book = Book.objects.create(title=title, description=description, photo=photo, category=category)
#         # book.user.add(user)
#         return Response({"posts": serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#         try:
#             instance = Book.objects.get(pk=pk)
#         except: return Response({"error": "Object does not exists"})
#         serializer = BookSerializers(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({"post": serializer.data})
#
#     def patch(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#         try:
#             instance = Book.objects.get(pk=pk)
#         except: return Response({"error": "Object does not exists"})
#         serializer = BookSerializers(data=request.data, instance=instance, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})


# class BookAPIView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class JWTView(ActionPermissionClassesMixin, viewsets.ModelViewSet):
    queryset = JWTokens.objects.all()
    serializer_class = JWTSerializers
    action_permission_classes = {
                                                    'create': [IsTokenAdminAuth],
                                                    'retrieve': [IsTokenAuth],
                                                    'list': [IsTokenAuth],
                                                    'update': [IsAuthorPostTokenAuth],
                                                    'partial_update': [IsAuthorPostTokenAuth],
                                                    'confirm_email': [AllowAny],
                                                    'destroy': [IsAuthorPostTokenAuth],
                                }

    def get_queryset(self):
        token = self.request.headers.get('Authorization').split("Benefix ")[1]
        jwt = JWTokens.objects.filter(token=token)
        count = jwt.first().count
        if count > 0:
            return jwt
        else:
            raise MissingTokenException


class BookAPIView(ActionPermissionClassesMixin, viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    action_permission_classes = {
                                                    'create': [IsTokenAdminAuth],
                                                    'retrieve': [IsTokenAuth],
                                                    'list': [IsTokenAuth],
                                                    'update': [IsAuthorPostTokenAuth],
                                                    'partial_update': [IsAuthorPostTokenAuth],
                                                    'confirm_email': [AllowAny],
                                                    'destroy': [IsAuthorPostTokenAuth],
                                }

    @action(methods=["get"], detail=True)
    def category(self, request, pk=None):
        category = Book.objects.get(pk=pk).category
        return Response({"category": category.name})

    @action(methods=["get"], detail=True)
    def users(self, request, pk=None):
        book_users = Book.objects.get(pk=pk).user.all()
        users = [user.username for user in book_users]
        return Response({"users": users})

    @action(methods=["get"], detail=False)
    def categories(self, request):
        category = Category.objects.all()
        return Response({"category": [{cat.pk: cat.name} for cat in category]})


