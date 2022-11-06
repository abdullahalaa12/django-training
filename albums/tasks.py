from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task()
def send_mail_task(to_email, artist, album):
    send_mail(subject="Congratulations!",
              message="Congratulations {artist} for uploading {album} album".format(
                                        artist=artist, album=album),
              from_email=settings.EMAIL_HOST_USER,
              recipient_list=[to_email]
              )
