import loguru
from rest_framework import serializers

from libraries.models import Book
from .models import JWTokens

# class BookSerializers(serializers.Serializer):
#     title = serializers.CharField(max_length=100)
#     description = serializers.CharField()
#     photo = serializers.ImageField()
#     time_create = serializers.DateField(read_only=True)
#     time_update = serializers.DateTimeField(read_only=True)
#     category = serializers.CharField()
#     user = serializers.StringRelatedField(many=True)

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'description', 'photo', 'time_create', 'time_update', 'is_published', 'category', 'user')

    # def create(self, validated_data):
    #     user = validated_data["user"]
    #     del validated_data["user"]
    #     book = Book.objects.create(**validated_data)
    #     for u in user:
    #         book.user.add(u)
    #         print("Добавил пользователя\n\n")
    #     return book
    #
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get("title", instance.title)
    #     instance.description = validated_data.get("description", instance.description)
    #
    #
    #     instance.photo = validated_data.get("photo", instance.photo)
    #     instance.category = validated_data.get("category", instance.category)
    #
    #
    #     instance.time_update = validated_data.get("time_update", instance.time_update)
    #     instance.is_published = validated_data.get("is_published", instance.is_published)
    #     instance.save()
    #     return instance

class JWTSerializers(serializers.ModelSerializer):
    class Meta:
        model = JWTokens
        fields = ('token', 'exp', 'iat', 'jti', 'time_update', 'minutes', 'count', 'isAdmin', 'user')

