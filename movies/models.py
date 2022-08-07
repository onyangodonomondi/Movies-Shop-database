from email.policy import default
from django.db import models
from django.utils import timezone

# Create your models here.


class Genre (models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rates = models.FloatField()
    downloadlink = models.URLField(max_length=300)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
