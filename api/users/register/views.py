from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from api.users.register.serializers import UserRegisterSerializer, SecretValidationSerializer


class UserRegisterApiView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()


class SecretValidationApiView(APIView):
    permission_classes = [AllowAny]
    serializer_class = SecretValidationSerializer

    def post(self, request):
        data = request.data
        serializer = SecretValidationSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
