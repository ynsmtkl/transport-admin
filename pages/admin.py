from django.contrib import admin

from api.users.models import UserConnect, UserType
from api.driving.models import Parent, Student, Driver, Bus

# Register your models here.
admin.site.register(UserConnect)
admin.site.register(UserType)
admin.site.register(Parent)
admin.site.register(Student)
admin.site.register(Driver)
admin.site.register(Bus)

