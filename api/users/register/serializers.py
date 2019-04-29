from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from api.users.models import Connect


class UserRegisterSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password_confirm = serializers.CharField(style={'input_type': 'password'}, write_only=True)

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
        ]

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        password_confirm = data.get('password_confirm')

        user = User.objects.filter(username=username)
        if user.exists():
            raise ValidationError("An account is already saved with this username")

        if password != password_confirm:
            raise ValidationError("The passwords mast match")

        return data

    def create(self, validated_data):
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        username = validated_data['username']
        password = validated_data['password']
        email    = validated_data['email']

        user = User(username=username, first_name=first_name, last_name=last_name, email=email)
        user.set_password(password)
        user.save()

        return validated_data


class SecretValidationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    secret = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Connect
        fields = ['email', 'secret', 'type']

    def validate(self, data):
        email = data.get('email')
        secret = data.get('secret')

        connect = Connect.objects.filter(email=email,secret=secret)

        if not connect.exists():
            raise ValidationError("Secret or email not valid, please try again")

        user = User.objects.filter(email=email)
        if user.exists():
            raise ValidationError("An account already saved with this email")

        return data
