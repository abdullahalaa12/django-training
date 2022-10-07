from django.db import models


# Create your models here.

class Artist(models.Model):
    stage_name = models.CharField(max_length=30, unique=True, blank=False, null=False)
    social_link = models.URLField(max_length=200, blank=True, null=False)

    class Meta:
        ordering = ['stage_name']

    def __str__(self):
        return self.stage_name
