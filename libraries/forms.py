from django import forms
from django.contrib.auth.forms import AuthenticationForm 

from captcha.fields import CaptchaField
from .models import *

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 'name': 'password',
                                                                 }))

    def validation(self, username, password):
        user = get_user_model()
        u = user.objects.filter(username=username)
        if u:
            return True
        else: return False

class BookPublishedForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "description", "photo", "category", "create_user"]

        widgets = {
            "title": forms.TextInput(attrs={
                "placeholder": "Заголовок",
                "class": "form-control",
            }),
            "description": forms.Textarea(attrs={
                "placeholder": "Описание",
                "class": "form-control",
            }),
            "create_user": forms.HiddenInput(attrs={
                "class": "hidden_input",
                "name": "hidden_input",
            }),
        }

    def save(self, user):
        book = super().save(commit=False)
        book.create_user = user
        book.save()
        return book

class ContactForm(forms.Form):
    content = forms.CharField(max_length=10000, widget=forms.Textarea(attrs={
        "class": "form-control"
    }))
    captcha = CaptchaField()
