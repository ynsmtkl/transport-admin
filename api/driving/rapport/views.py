from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from api.driving.rapport.serializers import GetStudentsSerializer


class GetStudentsApiView(APIView):
    permission_classes = [AllowAny]
    serializer_class = GetStudentsSerializer

    def post(self, request):
        data = request.data
        serializer = GetStudentsSerializer(data=data)

        if serializer.is_valid():
            new_data = serializer.validated_data
            return Response(data=new_data, status=HTTP_200_OK)
        return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)
