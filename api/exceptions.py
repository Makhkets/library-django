from rest_framework.exceptions import APIException

class MissingTokenException(APIException):
    status_code = 400
    default_detail = 'Вы потратили свое количество запросов'
    default_code = 'Количество запросов ограничено с вашего jwt токена'
