from django_filters import rest_framework as filters
from rest_framework.generics import ListAPIView
from django.http import JsonResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from rest_framework.viewsets import ModelViewSet

from books.filters import BookFilter
from books.models import Book
from books.serializers import BookSerializer


class BooksAPIView(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    authentication_classes = []
    permission_classes = [IsAuthenticated]

class SearchBookAPIView(ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = BookFilter
    def get(self, request):
        user = request.user
        print(user.token.payload['type'])
        return JsonResponse({}, status=status.HTTP_200_OK)
