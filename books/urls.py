from django.conf.urls import url
from django.urls import path
from rest_framework import routers

from books import views
from books.views import BooksAPIView

router = routers.DefaultRouter()

router.register(r'', BooksAPIView, basename='books')

urlpatterns = [
    url(r'^search/', views.SearchBookAPIView.as_view(), name='search'),
] + router.urls
