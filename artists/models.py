from django.db import models
from django.db.models import Count, Q
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


class ArtistManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().annotate(approved_albums=Count('album__id', filter=Q(album__is_approved=True)))


class Artist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    stage_name = models.CharField(max_length=30, unique=True, blank=False, null=False)
    social_link = models.URLField(max_length=200, blank=True, null=False)
    objects = ArtistManager()

    class Meta:
        ordering = ['stage_name']

    def __str__(self):
        return self.stage_name
