from django.http import JsonResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from rest_framework.viewsets import ModelViewSet


from books.models import Book
from books.serializers import BookSerializer


class BooksAPIView(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    authentication_classes = []
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        print(user.token.payload['type'])
        return JsonResponse({}, status=status.HTTP_200_OK)
