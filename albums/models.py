from django.db import models
from django.core.validators import FileExtensionValidator

from model_utils.models import TimeStampedModel
from artists.models import Artist

from imagekit.models import ImageSpecField
from pilkit.processors import Thumbnail


class ApprovedAlbumsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_approved=True)


class Album(TimeStampedModel):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    name = models.CharField(max_length=30, default="New Album")
    release_date = models.DateTimeField(blank=False, null=False)
    cost = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=False)
    is_approved = models.BooleanField(default=False, help_text='Approve the album if its name is not explicit')

    objects = models.Manager()
    approved_albums = ApprovedAlbumsManager()

    def __str__(self):
        return self.name


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    name = models.CharField(max_length=30, default=album.name)
    image = models.ImageField(blank=False, null=False, upload_to='static/albums/images')
    thumbnail = ImageSpecField(source='image',
                               processors=[Thumbnail(100, 50)],
                               format='JPEG',
                               options={'quality': 60})
    audio = models.FileField(blank=False, null=False,
                             upload_to='static/albums/audios',
                             help_text='.wav, .mp3',
                             validators=[FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])
