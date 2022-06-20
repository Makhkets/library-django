from django.db import models
from django.contrib.auth import get_user_model


class JWTokens(models.Model):
    token = models.CharField(max_length=1000, null=True, blank=True, editable=False)
    exp = models.CharField(max_length=100, null=True, blank=True, editable=False)
    iat = models.CharField(max_length=100, null=True, blank=True, editable=False)
    jti = models.CharField(max_length=100, null=True, blank=True, editable=False)
    time_update = models.DateTimeField(auto_now=True, editable=False)
    minutes = models.IntegerField()
    count = models.IntegerField()
    isAdmin = models.BooleanField(default=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)

    def __str__(self):
        return f"Token owner: {self.user.username}"



    # 'token_type': 'access',
    # 'exp': int(str(time.mktime(dt.timetuple()))[:-2]),
    # 'iat': dt_now,
    # 'jti': generate_charset(15),
    #
    # 'IsAdmin': IsAdmin,
    # 'count': count,
    # 'user_id': user_id,
    # 'nickname': nickname,
