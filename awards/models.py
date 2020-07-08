from django.db import models
from publishers.models import Publisher

# Create your models here.


class Award(models.Model):
    PERIOD = (
        ("biennial", "Biennial"),
        ("annual", "Annual"),
        ("monthly", "Monthly"),
        ("weekly", "Weekly"),
    )
    name = models.TextField(max_length=200)
    description = models.TextField()
    host = models.ForeignKey(Publisher)
    Nationality = models.TextField()
    period = models.TextField(choices=PERIOD, null=True)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
