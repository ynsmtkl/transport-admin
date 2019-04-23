from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

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
            Q(email=email) |
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

        return data


