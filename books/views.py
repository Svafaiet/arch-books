from django.http import JsonResponse
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from books.models import Book
from books.serializers import BookSerializer


class BooksAPIView(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    authentication_classes = []
    permission_classes = []
