from django.contrib import admin

from .models import Book, Category, User, Follower

admin.site.register(Book)
admin.site.register(Category)
admin.site.register(User)
admin.site.register(Follower)
