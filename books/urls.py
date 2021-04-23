from django.urls import path
from rest_framework import routers

from books.views import BooksAPIView

router = routers.DefaultRouter()

router.register(r'', BooksAPIView, basename='books')

urlpatterns = [
] + router.urls
