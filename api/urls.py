from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from djoser.urls import *
from api.views import *

router = routers.SimpleRouter()
router.register("token", JWTView)
router.register("books", BookAPIView)


urlpatterns = [
    path('v1/', include(router.urls), name="books_api"),
    path('auth/', include('djoser.urls')),

    path('auth/', include('djoser.urls.jwt')),

    path('', include(router.urls), name="router_urls")
]

