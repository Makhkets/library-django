from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm

from . import utils
from . import models

from loguru import logger
User = get_user_model()

class DefaultFormtMixin:
    form = None
    template = None
    reverse_url = None

    def get(self, request):
        return render(
                        request=request, 
                        template_name=self.template, 
                        context={"form": self.form}
        )

    def post(self, request):
        f = self.form(request.POST, request.FILES)
        if f.is_valid():
            f.save()
            return redirect(self.reverse_url)
        else:
            return HttpResponse(str(f.errors))

class AccountCreationForm(UserCreationForm):
    ''' Переопределенная форма UserCreationForm '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': ('Username')})
        self.fields['password1'].widget.attrs.update({'placeholder': ('Password')})        
        self.fields['password2'].widget.attrs.update({'placeholder': ('Repeat password')})

    class Meta:
        model = get_user_model()
        fields = ("username",)


class LoginMixin:
    template = None
    form = None
    reverse_url = None
    
    def get(self, request):
        return render(
                        request=request, 
                        template_name=self.template, 
                        context={"form": self.form}
        )
    
    def post(self, request):
        f = self.form(request.POST)
        username = request.POST.get("username")
        password = request.POST.get("password")
        if f.validation(username, password):
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return redirect(self.reverse_url)
        else:
            return render(
                        request=request, 
                        template_name=self.template, 
                        context={"form": self.form}
                    )


    #          Шпаргалки          #
    # request.user.is_authenticated