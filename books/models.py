from django.db import models


class Book(models.Model):
    title = models.CharField(unique=True, max_length=256)
    author = models.CharField(max_length=256)
    tags = models.ManyToManyField("books.Tag", related_name="books", related_query_name='books')


class Tag(models.Model):

    DEFAULT_TAGS = (
        "social",
        "novel",
        "educational",
        "science",
        "sci-fi"
    )

    name = models.CharField(max_length=64, primary_key=True)
