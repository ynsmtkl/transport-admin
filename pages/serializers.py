from rest_framework import serializers
from .models import Connect


class ConnectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connect
        fields = ['username', 'password']
