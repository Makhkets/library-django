from django.core.files.base import ContentFile
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model

from libraries.models import Book, Category
from api.models import JWTokens
from api.utils import generate_jwt

from loguru import logger as l
import requests

User = get_user_model()

class BookLibrariesTestCase(APITestCase):
    def setUp(self) -> None:
        def create_superuser():
            return User.objects.create_user(username="admin", password="admin", is_staff=True,
                                     is_active=True, is_superuser=True, email="rahimaliev999@gmail.com")

        def create_jwt():
            user = self.user
            jwt = generate_jwt(user_id=user.pk, nickname=user.username, minutes=10000, count=1000, IsAdmin=1)
            JWTokens.objects.create(
                token=jwt["token"],
                exp=jwt["encode"]["exp"],
                iat=jwt["encode"]["iat"],
                jti=jwt["encode"]["jti"],
                minutes=jwt["encode"]["minutes"],
                count=jwt["encode"]["count"],
                user_id=user.pk,
                isAdmin=True,
            )
            return jwt["token"]

        def add_category():
            return Category.objects.create(name="Фантастика")

        def add_books(category):
            return Book.objects.create(title="TEst", description="Описание книги",
                                       photo="images/2022/06/11/kniga_M6ggpqF.jpg",
                                       category=category)

        self.user = create_superuser()
        self.category = add_category()
        self.book = add_books(category=self.category)
        self.jwt = create_jwt()
        self.client.credentials(HTTP_AUTHORIZATION=f"Benefix {self.jwt}")

    def test_get_data(self):
        url = reverse("book-list")
        response = self.client.get(url)
        self.assertEqual(response.json()[0]["title"], "TEst")
        l.success("Тест | test_get_data | прошел успешно")

    def test_add_book(self):
        url = reverse("book-list")
        photo = requests.get("https://avatars.mds.yandex.net/get-zen_doc/1708012/pub_5e5e77c2170e395c41043f49_5e5e8290ac9a236dd3d946dd/scale_1200").content
        response = self.client.post(url, data={
            "title": "Book Test",
            "description": "Description",
            "category": 1,
            "user": [1],
            "photo": ContentFile(photo, "image.jpg")
        })

        self.assertEqual(response.data["title"], "Book Test")
        l.success("Тест | test_add_book | прошел успешно")