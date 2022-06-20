from loguru import logger as l
import requests
from pprint import pprint

class LibrariesApi:
    def __init__(self):
        self.session = requests.session()
        self.url = "http://127.0.0.1:8000/api/v1/books"
        self.url_token_info = "http://127.0.0.1:8000/api/auth/token/me"
        self.token = "Benefix eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc0OTQ5MTgzLCJpYXQiOjE2NTU2ODA3MjMsImp0aSI6IjlWNnV4TkZlaGI2Z3U2eSIsIklzQWRtaW4iOnRydWUsImNvdW50IjoiMzIxMzIiLCJ1c2VyX2lkIjoxLCJuaWNrbmFtZSI6ImFsaWV2In0.dFRmHHnwuxvPEjzQt1JRPvy1iGw5AG1U5crJutzsS9E"

    def save(self, response: str):
        with open("html.html", "w", encoding="utf-8") as file:
            file.write(response)

    def get(self):
        headers = {"authorization": self.token}
        response = requests.get(self.url, headers=headers)
        pprint(response.text)
        self.save(response.text)

    def post(self):
        filename = "1.jpg"
        with open(filename, "rb") as file:
            data = {
                "title": "Заголовок",
                "description": "Описание",
                "category": 1,
                "user": [1,2],
            }
            files = {'photo': file}
            r = requests.post("http://127.0.0.1:8000/api/v1/books", data=data, files=files)
            self.save(r.text)
            print(r.text)

    def put(self):
        pk = "1"
        data = {
            "title": "Последний шанс",
        }
        response = requests.patch("http://127.0.0.1:8000/api/v1/books/" + pk, data=data)
        print(response.text)
        self.save(response.text)

    def delete(self):
        pk = "7"
        data = {
            "title": "Последний шанс",
        }
        response = requests.delete("http://127.0.0.1:8000/api/v1/books/" + pk)
        print(response.text)
        self.save(response.text)




bot = LibrariesApi()
bot.get()
