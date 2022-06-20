import sys
import os

proj = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(proj)
os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'
import django
from django.core.mail import EmailMultiAlternatives
django.setup()

from libraries.models import *
from core.settings import EMAIL_HOST_USER

def main():
    with open("templates/index.html", "r", encoding="utf-8") as file:
        emails = Follower.objects.all()
        for email in emails:
            message = EmailMultiAlternatives("Заголовок", "Описание", EMAIL_HOST_USER, [email])
            message.attach_alternative(file.read(), "text/html")
            message.send()

main()
