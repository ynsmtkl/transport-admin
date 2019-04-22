from django.contrib.auth.models import User
from rest_framework import serializers
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
        fields = {
            'username',
            'password',
            'email',
            'token',
        }

        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }


