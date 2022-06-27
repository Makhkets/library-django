from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model

from libraries.models import Book
from api.models import JWTokens
from api.utils import generate_jwt

from loguru import logger as l
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
                isAdmin=1,
            )
            return jwt["token"]

        def add_books():
            return Book.objects.create(title="ТЕст", description="Описание книги",
                                       photo="images/2022/06/11/kniga_M6ggpqF.jpg",
                                       category=2, user=self.user, create_user=self.user)

        # title = models.CharField(max_length=100, verbose_name="Заголовок")
        # description = models.TextField(blank=True, verbose_name="Описание")
        # photo = models.ImageField(upload_to="images/%Y/%m/%d", verbose_name="Фото")
        # time_create = models.DateField(auto_now_add=True, verbose_name="Время создании")
        # time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
        # is_published = models.BooleanField(default=True, verbose_name="Публикация")
        # category = models.ForeignKey("Category", on_delete=models.PROTECT, verbose_name="Категории")
        # user = models.ManyToManyField(get_user_model(), null=True, blank=True, verbose_name="Пользователь книги")
        #
        # create_user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, related_name="create_user",
        #                                 verbose_name="Пользователь который добавил книгу",
        #                                 blank=True, null=True)


        self.user = create_superuser()
        self.jwt = create_jwt()
        self.client.credentials(HTTP_AUTHORIZATION=f"Benefix {self.jwt}")

    def test_get_data(self):
        url = reverse("book-list")
        response = self.client.get(url)
        l.success(response.data)