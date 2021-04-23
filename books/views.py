from django.http import JsonResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from books.models import Book
from books.permissions import BookPermission
from books.serializers import BookSerializer


class BooksAPIView(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated, BookPermission]

    def get(self, request):
        return JsonResponse({}, status=status.HTTP_200_OK)
