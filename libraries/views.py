from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin

import requests

from libraries.utils import *
from libraries.forms import *
from libraries.models import *
from core.settings import BOT_TOKEN

# Create your views here.



def index_libraries(request):
    return render(request, "libraries/index.html", {"category": 0})

def category_libraries(request, category):
    categories = Category.objects.filter(pk=category).all()
    return render(request, "libraries/index.html", {"category": category})

def DetailBook(request, id):
    book = Book.objects.get(id=id, is_published=1)
    return render(request, "libraries/detail.html", {"book": book})

@login_required
def AdminView(request):
    return render(request, "libraries/admin.html")

def ConfrimBook(request, id):
    book = Book.objects.get(id=id, is_published=1)
    if request.method == "POST":
        if request.user.telegram_id:
            book.user.add(request.user)
            book.is_published = 0
            book.save()
            return redirect("index")
        else: return HttpResponse("Ошибка, впишите свой телеграм айди в своем профиле")
    return render(request, "libraries/confrim.html", {"book": book})

@login_required
def DeleteBook(request, id):
    if request.method == "POST":
        book = Book.objects.get(id=id)
        book.delete()
    return redirect("admin")

@login_required
def ConfrimGetBook(request, id):
    if request.method == "POST":
        book = Book.objects.get(id=id)
        book.is_published = 1
        book.save()
    return redirect("admin")

@login_required
def NotifyBook(request, id):
    if request.method == "POST":
        book1 = Book.objects.get(id=id)
        book_user = book1.user.first()
        response = requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={book_user.telegram_id}&text=❗️ Верните книгу\n\nНазвание книги: {book1.title}\nКнига взята в: {book1.time_update}").json()['ok']
        return redirect("admin")

@login_required
def profile(request):
    if request.method == "POST":
        response = requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={request.POST.get('telegram_id')}&text=Тест введенных данных").json()['ok']
        if response:
            user = User.objects.get(id=request.user.id)
            user.telegram_id = request.POST.get('telegram_id')
            user.save()
            return render(request, "libraries/profile.html", {"success": "Данные успешно проверены и сохранены", "error": ""})
        else: return render(request, "libraries/profile.html", {"success": "", "error": "Неправильно веден айди или бот не активирован"}) 
            

    return render(request, "libraries/profile.html")  

class RegisterUser(DefaultFormtMixin, View):
    template = "registration/register.html"
    form = AccountCreationForm
    reverse_url = "index"

class LoginUser(LoginMixin, View):
    template = "registration/login.html"
    form = LoginForm
    reverse_url = "index"

class AddBook(LoginRequiredMixin, DefaultFormtMixin, View):
    template = "libraries/add_book.html"
    form = BookPublishedForm
    reverse_url = "index"
