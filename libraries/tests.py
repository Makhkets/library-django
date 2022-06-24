import django.http.response
from django.test import TestCase

from api.utils import generate_charset, decode_jwt
from libraries.models import User, Book

import requests
from loguru import logger as l
from bs4 import BeautifulSoup as bs


class LibrariesTestCase(TestCase):
    def setUp(self) -> None:
        self.site_url = "http://127.0.0.1:8000"
        self.password_current_user = "123"
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU2MzAzOTg0LCJpYXQiOjE2NTU3MTQ3ODQsImp0aSI6IjFHTndjeHY4SFhCMEF1ZiIsIklzQWRtaW4iOnRydWUsImNvdW50IjoiMTAwMDAiLCJ1c2VyX2lkIjoxLCJuaWNrbmFtZSI6ImFsaWV2In0.7aYrLKYgOpN_O4wQdMqt97vL7AJYQntISJ6DQJZN2Tk"



    def test_authorization(self):
        """ Тест аутентификации """
        def signup():
            pass

        def signin(username, password):
            pass

        data = signup()
        signin(username=data["username"], password=data["password"])

    def test_append_book(self):
        def add_through_form():
            pass
        def add_through_api():
            pass

        add_through_form()
        add_through_api()







