from django.db import models
# Create your models here.


class Character(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(max_length=200)

    description = models.TextField()

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
