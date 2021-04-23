from django_filters import rest_framework as filters
from rest_framework.generics import ListAPIView
from django.http import JsonResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from books.filters import BookFilter
from books.models import Book
from books.permissions import BookPermission
from books.serializers import BookSerializer


class BooksAPIView(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated, BookPermission]


class SearchBookAPIView(ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = BookFilter
