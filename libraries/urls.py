from django.urls import path
from .views import *

urlpatterns = [
    path('', index_libraries, name="libraries_index"),
    path('book/add/', AddBook.as_view(), name="add_book"),

    path('book/<int:id>/', DetailBook, name="view_book"),
    path('book/<int:id>/confrim/', ConfrimBook, name="confrim_book"),
    path('book/<int:id>/confrim-get/', ConfrimGetBook, name="confrim_get_book"),
    path('book/<int:id>/delete/', DeleteBook, name="delete_book"),
    path('book/<int:id>/notify/', NotifyBook, name="notify_book"),

    path('contact/', contact, name='contact'),
    path('profile/', profile, name="profile"),
    path('admin/', AdminView, name="admin"),
    path('following/', following, name='following'),
    path('category/<int:category>/', category_libraries, name="view_category"),
]
