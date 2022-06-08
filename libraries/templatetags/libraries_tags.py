from django import template
from django.db.models import Q

from libraries.models import *
from loguru import logger

register = template.Library()

@register.simple_tag()
def get_books(request, selected=0):
    search_query = request.GET.get("search", "")
    if search_query:
        return Book.objects.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query)).filter(is_published=1)
    if selected == 0:
        return Book.objects.filter(is_published=1)
    else:
        return Book.objects.filter(category__pk=selected).filter(is_published=1).all()

@register.inclusion_tag(filename="user_tags/categories_list.html")
def show_categories(selected=0):
    categories = Category.objects.all()
    return {"categories": categories, "selected": selected}
