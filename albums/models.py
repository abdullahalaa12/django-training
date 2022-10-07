from django.db import models
from django.utils import timezone

# Create your models here.
from artists.models import Artist


class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    name = models.CharField(max_length=30, default="New Album")
    creation_date = models.DateTimeField(default=timezone.now)
    release_date = models.DateTimeField(blank=False, null=False)
    cost = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=False)
