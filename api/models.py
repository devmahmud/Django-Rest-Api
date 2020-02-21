from django.db import models
from django.utils import timezone


class Book(models.Model):
    title = models.CharField(max_length=36, unique=True)
    description = models.TextField(max_length=256, blank=True)
    price = models.DecimalField(default=0, max_digits=3, decimal_places=2)
    published = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='covers/', blank=True)

    number = models.OneToOneField(
        to="BookNumber", blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class BookNumber(models.Model):
    isbn_10 = models.CharField(max_length=10, blank=True)
    isbn_13 = models.CharField(max_length=13, blank=True)

    def __str__(self):
        if self.isbn_10:
            return self.isbn_10
        else:
            return self.isbn_13


class Character(models.Model):
    name = models.CharField(max_length=30)
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="characters")

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    books = models.ManyToManyField(Book, related_name="authors")

    def __str__(self):
        return self.surname
