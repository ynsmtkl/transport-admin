from django.contrib.auth import authenticate, login
from django.utils import timezone

from rest_framework import viewsets, status
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from ebaytrading import settings
from pages.models import Connect
from pages.serializers import ConnectSerializer, UserLoginSerializer


class ConnectView(viewsets.ModelViewSet):
    queryset = Connect.objects.all()
    serializer_class = ConnectSerializer

    def get_queryset(self):
        username = self.request.data.get("username")
        password = self.request.data.get('password')

        # user = authenticate(username='yns', password='123')

        # if user is not None:
        #     if user.is_active:
        #         # login(self.request, user)
        #         queryset = Connect.objects.filter(username='yns')
        #     else:
        #         queryset = Connect.objects.none()
        # else:
        #     queryset = Connect.objects.none()

        # connect = Connect(username=username, password=password, date=timezone.now())
        #
        # connect.save()
        queryset = Connect.objects.filter(username=username, password=password)
        return queryset


def home(request):
    from .ebay.findbykeywords import findbykeywords
    from .ebay.fetchtoken import get_token, get_session_id
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


def userlogin(request):
    username = request.POST['username']
    password = request.POST['password']

    # userconnect = Connect(username=username, password=password, date=timezone.now())

    # userconnect.save()

    # return JsonResponse({'username': username, 'email': password})

    user = authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            login(request, user)
            return JsonResponse({'message': 'success'})
        else:
            return JsonResponse({'message': 'Failed is not active'})
    else:
        return JsonResponse({'message': 'Failed'})


class UserLoginApiView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

