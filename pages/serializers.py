from django.contrib.auth.models import User
from django.db.models import Q
from django.utils.encoding import force_text
from rest_framework import serializers, status
from rest_framework.exceptions import ValidationError, APIException

from .models import Connect


class ConnectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connect
        fields = ['username', 'password']


class UserLoginSerializer(serializers.ModelSerializer):
    token = serializers.CharField(allow_blank=True, read_only=True)
    username = serializers.CharField()
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'password',
            'email',
            'token',
        ]

        extra_kwargs = {
            "password":{
                "write_only": True
            }
        }

    def validate(self, data):
        user_obj = None
        email = data.get("email")
        username = data.get("username")
        password = data['password']
        if not email and not username:
            raise ValidationError("Email or Username is required to login")
        user = User.objects.filter(
            Q(username=username)
        ).distinct()
        user = user.exclude(email__isnull=True, email__iexact='')
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("This email or username is not valid")

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("password is not correct, please try again!")

        data["token"] = "some random token"
        data["id"] = user_obj.id

        return data


class UserRegisterSerializer(serializers.ModelSerializer):
    token = serializers.CharField(allow_blank=True, read_only=True)
    username = serializers.CharField()
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'password',
            'email',
        ]

        extra_kwargs = {
            "password":{
                "write_only": True
            }
        }

    def validate(self, data):
        user_obj = None
        email = data.get("email")
        username = data.get("username")
        password = data['password']
        if not email and not username:
            raise CustomValidation("username is required to login",
                                   'username', status_code=status.HTTP_409_CONFLICT)
        user = User.objects.filter(
            Q(username=username)
        ).distinct()
        user = user.exclude(email__isnull=True, email__iexact='')
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise CustomValidation("This username is not valid",
                                   'username', status_code=status.HTTP_409_CONFLICT)

        if user_obj:
            if not user_obj.check_password(password):
                raise CustomValidation("password is not correct, please try again!",
                                       'password', status_code=status.HTTP_406_NOT_ACCEPTABLE)

        data["token"] = "some random token"
        data["id"] = user_obj.id

        return data


class CustomValidation(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = 'A server error occurred.'

    def __init__(self, detail, field, status_code):
        if status_code is not None:self.status_code = status_code
        if detail is not None:
            self.detail = {field: force_text(detail)}
        else: self.detail = {'detail': force_text(self.default_detail)}
