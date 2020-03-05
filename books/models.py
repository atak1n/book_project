from django.db import models
from django.urls import reverse


class Book(models.Model):
    title = models.CharField('Book title', max_length=50)
    year = models.PositiveIntegerField()
    author = models.CharField(max_length=50)
    price = models.FloatField('Price of the book')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('books_detail', args=[str(self.id)])
