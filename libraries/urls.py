from django.urls import path
from .views import *

urlpatterns = [
    path('', index_libraries, name="libraries_index"),
    path('book/add/', AddBook.as_view(), name="add_book"),
    path('book/<int:id>/', DetailBook, name="view_book"),
    path('book/<int:id>/confrim', ConfrimBook, name="confrim_book"),
    path('category/<int:category>', category_libraries, name="view_category"),
]
