from django import template
from django.db.models import Q
from django.core.paginator import Paginator

from libraries.models import *

from loguru import logger

register = template.Library()

@register.simple_tag()
def get_books(request, selected=0, filter=None):
    search_query = request.GET.get("search", "")
    if search_query:
        return Book.objects.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query)).filter(is_published=1)
    if filter:
        books = Book.objects.filter(is_published=0)
        paginator = Paginator(books, 3)
        page_number = request.GET.get("page")
        return paginator.get_page(page_number)
    if selected == 0:
        books = Book.objects.filter(is_published=1)
        paginator = Paginator(books, 3)
        page_number = request.GET.get("page")
        return paginator.get_page(page_number)
    else:
        books = Book.objects.filter(category__pk=selected).filter(is_published=1).all()
        paginator = Paginator(books, 3)
        page_number = request.GET.get("page")
        return paginator.get_page(page_number)

@register.inclusion_tag(filename="user_tags/categories_list.html")
def show_categories(selected=0):
    categories = Category.objects.all()
    return {"categories": categories, "selected": selected}
