from django.db import models
from awards.models import Award
from books.models import Book
from characters.models import Character
from crews.models import Crew
from genres.models import Genres
from publishers.models import Publisher
# Create your models here.


class Score(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    crew = models.ForeignKey(Crew, on_delete=models.CASCADE, null=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True)

    score = models.DecimalField(max_digits=2, decimal_places=0)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    id = models.PositiveIntegerField(primary_key=True)

    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    award = models.ForeignKey(Award, on_delete=models.CASCADE, null=True)
    character = models.ForeignKey(Character, on_delete=models.CASCADE, null=True)
    crew = models.ForeignKey(Crew, on_delete=models.CASCADE, null=True)
    genre = models.ForeignKey(Genres, on_delete=models.CASCADE, null=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True)

    title = models.CharField(max_length=100)
    text = models.TextField(2500)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    id = models.PositiveIntegerField(primary_key=True)

    award = models.ForeignKey(Award, on_delete=models.CASCADE, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    crew = models.ForeignKey(Crew, on_delete=models.CASCADE, null=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True)

    title = models.CharField(max_length=100)
    text = models.TextField(2500)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    id = models.PositiveIntegerField(primary_key=True)

    award = models.ForeignKey(Award, on_delete=models.CASCADE, null=True)
    character = models.ForeignKey(Character, on_delete=models.CASCADE, null=True)

    liked = models.NullBooleanField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

