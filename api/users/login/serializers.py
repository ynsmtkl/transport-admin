from django.contrib.auth.models import User
from django.db.models import Q
from django.utils.encoding import force_text
from rest_framework import serializers, status
from rest_framework.exceptions import ValidationError, APIException


class UserLoginSerializer(serializers.ModelSerializer):
    token = serializers.CharField(allow_blank=True, read_only=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    email = serializers.EmailField(allow_blank=True, read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'password',
            'email',
            'token',
        ]

    def validate(self, data):
        user_obj = None
        username = data.get("username")
        password = data['password']
        if not password and not username:
            raise ValidationError("Password and Username are required to login")
        user = User.objects.filter(
            Q(username=username)
        ).distinct()

        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("This username is not valid")

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("password is not correct, please try again!")

        data["token"] = "some random token"
        data["id"] = user_obj.id
        data["email"] = user_obj.email

        return data

