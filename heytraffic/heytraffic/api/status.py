from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from datetime import datetime


class StatusAPIView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request):
        return Response({
            "status": "awesome",
            "datetime": datetime.now(),
        })
