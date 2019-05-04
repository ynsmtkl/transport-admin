from datetime import datetime

from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from api.driving.models import Bus
from api.users.models import UserConnect


class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    email = serializers.EmailField(allow_blank=True, read_only=True)
    user_type = serializers.CharField(allow_blank=True, read_only=True)
    driver = serializers.EmailField(allow_blank=True, read_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'password',
            'email',
            'user_type',
            'driver',
        )
        extra_kwargs = {
            'first_name': {
                'read_only': True
            },
            'last_name':{
                'read_only': True
            }
        }

    def validate(self, data):
        user_obj = None
        connect_obj = None
        bus_obj = None

        username = data.get("username")
        password = data['password']
        if not password and not username:
            raise ValidationError("Password and Username are required to login")
        user = User.objects.filter(username=username).distinct()

        if user.exists():
            user_obj = user.first()
            if not user_obj.is_active:
                raise ValidationError("This account is not active")
        else:
            raise ValidationError("This username is not valid")

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Password is not correct, please try again!")

            # Looking for the type of the user
            connect = UserConnect.objects.filter(email=user_obj.email)
            if not connect.exists():
                raise ValidationError("We can't found the type of this account, please contact your admin")
            connect_obj = connect.first()

            date_start = datetime(connect_obj.date_star.year, connect_obj.date_star.month, connect_obj.date_star.day)
            date_end = datetime(connect_obj.date_end.year, connect_obj.date_end.month, connect_obj.date_end.day)

            if date_start > datetime.now() or date_end < datetime.now():
                raise ValidationError("This account is out of date, please contact your admin")

            if connect_obj.userType.type == "Parent":
                bus = Bus.objects.filter(student__user_connect__email=connect_obj.email)
                if not bus.exists():
                    raise ValidationError("No affected driver for this student")

                bus_obj = bus.first()

        data["id"] = user_obj.id
        data["email"] = user_obj.email
        data["first_name"] = user_obj.first_name
        data["last_name"] = user_obj.last_name
        data["user_type"] = connect_obj.userType
        data["driver"] = bus_obj.driver

        return data


class VerifyUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)

    class Meta:
        model  = User
        fields = (
            'id',
            'username',
            'email'
        )

        extra_kwargs = {
            'email': {
                'read_only': True
            }
        }

    def validate(self, data):
        username = data.get('username')
        user = User.objects.filter(username=username)

        if not user.exists():
            raise ValidationError("This account was removed, please contact your admin!")

        user_obj = user.first()
        if not user_obj.is_active:
            raise ValidationError("This account is not active, please contact your admin")

        connect = UserConnect.objects.filter(email=user_obj.email)
        if connect.exists():
            connect_obj = connect.first()

            date_start = datetime(connect_obj.date_star.year, connect_obj.date_star.month, connect_obj.date_star.day)
            date_end = datetime(connect_obj.date_end.year, connect_obj.date_end.month, connect_obj.date_end.day)

            if date_start > datetime.now() or date_end < datetime.now():
                raise ValidationError("This account is out of date, please contact your admin")

        data['id'] = user_obj.id
        data['email'] = user_obj.email

        return data

