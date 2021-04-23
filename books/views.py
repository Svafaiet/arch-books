from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView


class Books(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        return JsonResponse({}, status=status.HTTP_200_OK)
