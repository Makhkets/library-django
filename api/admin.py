import loguru
from django.contrib import admin

# Register your models here.
from .models import JWTokens
from .utils import generate_jwt
from libraries.models import User

class SaveData(admin.ModelAdmin):
    list_display = ('id', 'exp', 'iat', 'jti', 'time_update', 'minutes', 'count', 'isAdmin', 'user', 'token')
    search_fields = ('id', 'token')
    list_editable = ('minutes', 'count')
    list_filter = ('id', 'iat', 'time_update', 'count', 'minutes')
    def save_model(self, request, obj, form, change):
        if obj.token:
            pass
        else:
            minutes = request.POST.get("minutes")
            count = request.POST.get("count")
            isAdmin = bool(request.POST.get("isAdmin"))
            user = User.objects.get(pk=int(request.POST.get("user")))
            JWT = generate_jwt(user_id=user.pk, nickname=user.username, minutes=int(minutes), count=count, IsAdmin=isAdmin)
            obj.token = JWT["token"]
            obj.exp = JWT["encode"]["exp"]
            obj.iat = JWT["encode"]["iat"]
            obj.jti = JWT["encode"]["jti"]
            obj.save()
        super().save_model(request, obj, form, change)

admin.site.register(JWTokens, SaveData)