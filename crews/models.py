from django.db import models
from awards.models import Award

# Create your models here.


class Crew(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.TextField(max_length=200)
    last_name = models.TextField(max_length=200)
    nick_name = models.TextField(max_length=200)
    birth_place = models.TextField(max_length=100)
    birth_date = models.DateTimeField()
    resident = models.TextField(default="earth")
    description = models.TextField()
    job = models.ManyToManyField(
        'Job',
        through='CrewJob',
        through_fields=('crew', 'job'),
        on_delete=models.CASCADE
    )
    awards = models.ManyToManyField(Award, on_delete=models.CASCADE)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Job(models.Model):
    name = models.TextField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


class CrewJob(models.Model):
    crew = models.ForeignKey(Crew, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    start_date = models.DateField(null=True)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
