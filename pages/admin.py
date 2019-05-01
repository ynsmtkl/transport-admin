from django.contrib import admin
from api.users.models import UserConnect, UserType

# Register your models here.
admin.site.register(UserConnect)
admin.site.register(UserType)
