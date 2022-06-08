"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from django.contrib.auth.urls import *
from django.conf.urls.static import static

from core import settings # Строка служит как мини документация, для просмотра ссылок которые мне доступны
from libraries.views import *

def redirect_libraries(request):
    return redirect("libraries_index")

urlpatterns = [
    path('', redirect_libraries, name="index"),
    path('admin/', admin.site.urls),
    path('accounts/login/', LoginUser.as_view(), name='login'),
    path('accounts/register/', RegisterUser.as_view(), name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('libraries/', include('libraries.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
