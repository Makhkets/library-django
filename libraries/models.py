import time
from datetime import datetime, timedelta
import string
import secrets

import loguru
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

import jwt
from core import settings

def generate_charset(length: int):
    return "".join(
        secrets.choice(string.digits + string.ascii_letters) for _ in range(length)
    )

class User(AbstractUser):
    telegram_id = models.CharField(max_length=100, null=True, blank=True, verbose_name="Телеграм айди")
    def __str__(self):
        return self.username

class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    description = models.TextField(blank=True, verbose_name="Описание")
    photo = models.ImageField(upload_to="images/%Y/%m/%d", verbose_name="Фото")
    time_create = models.DateField(auto_now_add=True, verbose_name="Время создании")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    category = models.ForeignKey("Category", on_delete=models.PROTECT, verbose_name="Категории")
    user = models.ManyToManyField(get_user_model(), null=True, blank=True, verbose_name="Пользователь книги")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('view_book', kwargs={'id': self.pk})
    def confrim_book(self):
        return reverse('confrim_book', kwargs={"id": self.pk})
    def delete_book(self):
        return reverse('delete_book', kwargs={"id": self.pk})
    def confrim_get_book(self):
        return reverse('confrim_get_book', kwargs={"id": self.pk})
    def notify_book(self):
        return reverse('notify_book', kwargs={"id": self.pk})

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("view_category", kwargs={"category": self.pk})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Follower(models.Model):
    email = models.EmailField()
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Подписчики на рассылку"
        verbose_name_plural = "Подписчики на рассылку"
