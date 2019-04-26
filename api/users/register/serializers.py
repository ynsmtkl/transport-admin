from django.contrib.auth.models import User
from django.db.models import Q
from django.utils.encoding import force_text
from rest_framework import serializers, status
from rest_framework.exceptions import ValidationError, APIException

from api.users.models import Connect


class UserRegisterSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password_confirm = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    secret = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'username',
            'password',
            'password_confirm',
            'email',
            'secret',
        ]

    # def validate_password_confirm(self, value):
    #     data = self.initial_data
    #     password = data.get('password')
    #     password_confirm = value
    #
    #     if password != password_confirm:
    #         raise ValidationError("The passwords doesn't match, please confirm your password")
    #
    #     return value

    # def validate_username(self, value):
    #     user = User.objects.filter(username=value)
    #
    #     if user.exists():
    #         raise ValidationError("An account is already saved with this username")
    #
    #     return value

    # def validate_email(self, value):
    #     user = User.objects.filter(email=value)
    #
    #     if user.exists():
    #         raise ValidationError("An account is already saved with this email")
    #
    #     return value

    def validate(self, data):
        self.email = data.get('email')
        self.secret = data.get('secret')

        connect = Connect.objects.filter(email=self.email, secret=self.secret)
        if not connect.exists():
            raise ValidationError("This secret code is not valid, please contact your admin")

        return data

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        email    = validated_data['email']

        user = User(username=username, email=email)
        user.set_password(password)
        user.save()

        return validated_data
