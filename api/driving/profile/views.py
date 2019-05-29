from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from api.driving.profile.serializers import EditParentSerializer, EditDriverSerializer, EditStudentSerializer


class EditUserApiView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = EditParentSerializer


class EditDriverApiView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = EditDriverSerializer


class EditStudentApiView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = EditStudentSerializer
