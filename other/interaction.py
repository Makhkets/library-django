from loguru import logger as l
import requests
from pprint import pprint

class LibrariesApi:
    def __init__(self):
        self.session = requests.session()
        self.url = "http://127.0.0.1:8000/api/v1/books"
        self.url_token_info = "http://127.0.0.1:8000/api/token"
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU2MzAzOTg0LCJpYXQiOjE2NTU3MTQ3ODQsImp0aSI6IjFHTndjeHY4SFhCMEF1ZiIsIklzQWRtaW4iOnRydWUsImNvdW50IjoiMTAwMDAiLCJ1c2VyX2lkIjoxLCJuaWNrbmFtZSI6ImFsaWV2In0.7aYrLKYgOpN_O4wQdMqt97vL7AJYQntISJ6DQJZN2Tk"

    def save(self, response: str):
        with open("html.html", "w", encoding="utf-8") as file:
            file.write(response)

    def get(self):
        headers = {"authorization": "Benefix " + self.token}
        response = requests.get(self.url_token_info, headers=headers)
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
