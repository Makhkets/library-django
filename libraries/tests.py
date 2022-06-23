from django.test import TestCase
from api.utils import generate_charset, decode_jwt

from libraries.models import User

import requests
from loguru import logger as l
from bs4 import BeautifulSoup as bs


class LibrariesTestCase(TestCase):
    def setUp(self) -> None:
        self.site_url = "http://127.0.0.1:8000"
        self.password_current_user = "123"
        self.libraries_client = requests.session()
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU2MzAzOTg0LCJpYXQiOjE2NTU3MTQ3ODQsImp0aSI6IjFHTndjeHY4SFhCMEF1ZiIsIklzQWRtaW4iOnRydWUsImNvdW50IjoiMTAwMDAiLCJ1c2VyX2lkIjoxLCJuaWNrbmFtZSI6ImFsaWV2In0.7aYrLKYgOpN_O4wQdMqt97vL7AJYQntISJ6DQJZN2Tk"
        self.libraries_client.headers.update({"authorization": "Benefix " + self.token})


    def test_authorization(self):
        """ Тест аутентификации """
        def signup():
            username = generate_charset(10)
            password = generate_charset(10)
            response = self.libraries_client.post(self.site_url + "/api/auth/users/", data={
                "username": username,
                "password": password
            }).json()
            self.assertEqual(response["username"], username) # Проверка на созданный объект
            l.success("Пользователь успешно создан")
            return {"username": username, "password": password, "id": response["id"]}

        def signin(username, password):
            response = self.libraries_client.get(self.site_url + "/accounts/login")
            soup = bs(response.text, "lxml")
            csrf_token = soup.find("input", {"name": "csrfmiddlewaretoken"}).get("value")
            r = self.libraries_client.post(self.site_url + "/accounts/login/", data={"csrfmiddlewaretoken": csrf_token,
                                                                                    "username": username,
                                                                                    "password": password})
            title = bs(r.text, "lxml").find("title").text.strip()
            self.assertEqual(title, "Главная")
            l.success("Пользователь успешно прошел этап авторизации")

        def delete(id):
            r = self.libraries_client.delete(self.site_url + "/api/auth/users/" + str(id) + "/", data={
                "current_password": self.password_current_user,
            })
            if len(r.text) == 0:
                self.assertEqual(len(r.text), 0) # Проверка на удаление объекта
                l.info("Пользователь успешно удален")

        data = signup()
        signin(username=data["username"], password=data["password"])
        delete(id=data["id"])

    def test_append(self):
        pass