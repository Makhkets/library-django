import loguru
from django.contrib import admin

# Register your models here.
from .models import JWTokens
from .utils import generate_jwt
from libraries.models import User

class SaveData(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
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