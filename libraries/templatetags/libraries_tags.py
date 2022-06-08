from django import template
from libraries.models import *

register = template.Library()

@register.simple_tag()
def get_books(selected=0):
    if selected == 0:
        return Book.objects.all()
    else:
        return Book.objects.filter(category__pk=selected).all()

@register.inclusion_tag(filename="user_tags/categories_list.html")
def show_categories(selected=0):
    categories = Category.objects.all()
    return {"categories": categories, "selected": selected}