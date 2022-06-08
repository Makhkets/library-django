from django.contrib import admin

from .models import Book, Category

admin.site.register(Book)
admin.site.register(Category)
