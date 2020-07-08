from django.db import models
from characters.models import Character
from genres.models import Genres
from crews.models import CrewJob
from awards.models import Award
from publishers.models import Publisher, Publishing
from tanzimat.Constants import SERIES_REL_TYPE, PARENT_REL_TYPE
# Create your models here.


class Series(models.Model):
    name = models.TextField(max_length=200)
    description = models.TextField()
    parent_series = models.ForeignKey('self', on_delete=models.CASCADE, null=True, default=None)
    place = models.DecimalField(max_digits=3, decimal_places=0, null=True, default=None)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Book(models.Model):

    id = models.BigAutoField(primary_key=True)
    name = models.TextField(max_length=200)
    description = models.TextField()
    isbn = models.DecimalField(max_digits=13, decimal_places=0, unique=True)
    language = models.CharField(max_length=50)
    series = models.ForeignKey(Series, on_delete=models.CASCADE, null=True, default=None)
    series_rel_type = models.CharField(max_length=100, choices=SERIES_REL_TYPE, null=True, default=None)
    place_in_series = models.DecimalField(max_digits=3, decimal_places=0, null=True, default=None)
    parent_book = models.ForeignKey('self', on_delete=models.CASCADE, null=True, default=None)
    parent_rel = models.TextField(max_length=500, choices=PARENT_REL_TYPE)
    genres = models.ManyToManyField(Genres, on_delete=models.CASCADE, null=True)
    awards = models.ManyToManyField(Award, on_delete=models.CASCADE)

    crews = models.ManyToManyField(CrewJob, on_delete=models.CASCADE)

    publisher = models.ManyToManyField(
        'Publisher',
        through='Publishing',
        through_fields=('book', 'publisher'),
        on_delete=models.CASCADE
    )

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Chapter(models.Model):
    name = models.TextField(max_length=200)
    description = models.TextField()
    book = models.ForeignKey(Series, on_delete=models.CASCADE)
    place_in_book = models.DecimalField(max_digits=3, decimal_places=0)
    character = models.ManyToManyField(Character, null=True)
    time = models.BigIntegerField(default=2)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
