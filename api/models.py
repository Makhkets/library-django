from django.db import models
from django.contrib.auth import get_user_model


class JWTokens(models.Model):
    token = models.CharField(max_length=1000, null=True, blank=True, editable=False, verbose_name="Токен")
    exp = models.CharField(max_length=100, null=True, blank=True, editable=False, verbose_name="Время токена")
    iat = models.CharField(max_length=100, null=True, blank=True, editable=False, verbose_name="Iat")
    jti = models.CharField(max_length=100, null=True, blank=True, editable=False, verbose_name="Jti")
    time_update = models.DateTimeField(auto_now=True, editable=False, verbose_name="Последний запрос")
    minutes = models.IntegerField(verbose_name="На какой срок был создан токен")
    count = models.IntegerField(verbose_name="Количество запросов")
    isAdmin = models.BooleanField(default=False, verbose_name="Является ли админским")
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, verbose_name="Пользователь токена")

    def __str__(self):
        return f"Token owner: {self.user.username}"

    class Meta:
        verbose_name = "Токен"
        verbose_name_plural = "Токены"


    # 'token_type': 'access',
    # 'exp': int(str(time.mktime(dt.timetuple()))[:-2]),
    # 'iat': dt_now,
    # 'jti': generate_charset(15),
    #
    # 'IsAdmin': IsAdmin,
    # 'count': count,
    # 'user_id': user_id,
    # 'nickname': nickname,
