from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View

from libraries.utils import *
from libraries.forms import *
from libraries.models import *

# Create your views here.
def index_libraries(request):
    return render(request, "libraries/index.html", {"category": 0})

def category_libraries(request, category):
    categories = Category.objects.filter(pk=category).all()
    return render(request, "libraries/index.html", {"category": category})




class RegisterUser(DefaultFormtMixin, View):
    template = "registration/register.html"
    form = AccountCreationForm
    reverse_url = "index"

class LoginUser(LoginMixin, View):
    template = "registration/login.html"
    form = LoginForm
    reverse_url = "index"

class AddBook(DefaultFormtMixin, View):
    template = "libraries/add_book.html"
    form = BookPublishedForm
    reverse_url = "index"

def DetailBook(request, id):
    book = Book.objects.get(id=id)
    return render(request, "libraries/detail.html", {"book": book})
