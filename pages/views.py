from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from ebaytrading import settings
from pages.serializers import UserLoginSerializer, UserRegisterSerializer


def home(request):
    from .ebay.findbykeywords import findbykeywords
    return render(request, "home.html", {"findbykeywords": findbykeywords})


def about(request):
    from pages.namer import namer
    return render(request, "about.html", {"aboutme": namer})


def contact(request):
    return render(request, "contact.html", {})


def get_session(request):
    from .ebay.fetchtoken import get_session_id
    return render(request, "home.html", {"session_id": get_session_id, "runame": settings.URNAME})


def get_token(request):
    from .ebay.fetchtoken import get_token
    return render(request, "home.html", {"token": get_token})


class UserLoginApiView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request):
        data = request.data
        serializer = UserLoginSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class UserRegisterApiView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserRegisterSerializer

    def post(self, request):
        data = request.data
        serializer = UserRegisterSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

