from celery import Celery, shared_task
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone

from artists.models import Artist

app = Celery()


@shared_task()
def send_mail_task(to_email, artist, album):
    send_mail(subject="Congratulations!",
              message="Congratulations {artist} for uploading {album} album".format(
                                        artist=artist, album=album),
              from_email=settings.EMAIL_HOST_USER,
              recipient_list=[to_email]
              )


@app.task
def check_artists_created_albums_past_30_days():
    artists = Artist.objects.select_related('user').all()
    for artist in artists:
        if artist.album_set.filter(created__gte=timezone.now() - timezone.timedelta(days=30)).count() == 0:
            send_mail(subject="Musicplatform",
                      message="{artist} It's been more than 30 days since you created an album".format(
                          artist=artist.stage_name),
                      from_email=settings.EMAIL_HOST_USER,
                      recipient_list=[artist.user.email]
                      )
