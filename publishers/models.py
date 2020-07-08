from django.db import models
from awards.models import Award
from books.models import Book

# Create your models here.


class Publisher(models.Model):
    name = models.TextField(max_length=200)
    nationality = models.TextField(max_length=1000)
    foundation_date = models.DateField()
    address = models.TextField(max_length=500)
    website = models.TextField(max_length=200)
    awards = models.ManyToManyField(Award, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Publishing(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publish_date = models.DateField()
    publish_number = models.IntegerField(default=1)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
