from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    tags = models.ManyToManyField("books.Tag", related_name="books", related_query_name='books')


class Tag(models.Model):
    DEFAULT_TAGS = [
        ('sci-fi', 'علمی تخیلی'),
        ('historical', 'تاریخی'),
        ('educational', 'آموزشی'),
        ('science', 'علمی'),
        ('social', 'اجتماعی'),
        ('novel', 'رمان'),
    ]

    name = models.CharField(max_length=64, choices=DEFAULT_TAGS, primary_key=True)
