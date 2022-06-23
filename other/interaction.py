from loguru import logger as l
import requests
from pprint import pprint

class LibrariesApi:
    def __init__(self):
        self.session = requests.session()
        self.url = "http://127.0.0.1:8000/api/v1/books/1"
        self.url_token_info = "http://127.0.0.1:8000/api/token"
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU2MzAzOTg0LCJpYXQiOjE2NTU3MTQ3ODQsImp0aSI6IjFHTndjeHY4SFhCMEF1ZiIsIklzQWRtaW4iOnRydWUsImNvdW50IjoiMTAwMDAiLCJ1c2VyX2lkIjoxLCJuaWNrbmFtZSI6ImFsaWV2In0.7aYrLKYgOpN_O4wQdMqt97vL7AJYQntISJ6DQJZN2Tk"

    def save(self, response: str):
        with open("html.html", "w", encoding="utf-8") as file:
            file.write(response)

    def get(self):
        headers = {"authorization": "Benefix " + self.token}
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
            r = requests.post("http://127.0.0.1:8000/api/v1/books/", data=data, files=files, headers={"Authorization": "Benefix " + self.token})
            self.save(r.text)
            print(r.text)

    def patch(self):
        pk = "45"
        data = {
            "title": "Последний шанс",
        }
        headers = {"authorization": "Benefix " + self.token}
        response = requests.patch("http://127.0.0.1:8000/api/v1/books/" + pk + "/", data=data, headers=headers)
        print(response.text)
        self.save(response.text)

    def delete(self):
        pk = "45"
        data = {
            "title": "Последний шанс",
        }
        headers = {"authorization": "Benefix " + self.token}

        response = requests.delete("http://127.0.0.1:8000/api/v1/books/" + pk + "/", headers=headers)
        print(response.text)
        self.save(response.text)




bot = LibrariesApi()
bot.delete()
