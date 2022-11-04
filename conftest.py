import pytest
from rest_framework.test import APIClient
from knox.models import AuthToken

from django.contrib.auth import get_user_model
from django.utils import timezone
from artists.models import Artist
from albums.models import Album

User = get_user_model()


@pytest.fixture
def user_data_1():
    user = User.objects.create_user(username='admin', password='123', email='admin@gmail.com', bio='Owner')
    return user


@pytest.fixture
def user_data_2():
    user = User.objects.create_user(username='abdullah', password='456', email='abdullah@gmail.com', bio='SWE')
    return user


@pytest.fixture
def artist_data_1(user_data_1):
    artist = Artist.objects.create(stage_name='Michael Jackson',
                                   social_link='https://twitter.com/michaeljackson',
                                   user=user_data_1)
    return artist


@pytest.fixture
def album_data_1(artist_data_1):
    artist = Album.objects.create(name='Bad',
                                  release_date=timezone.now(),
                                  cost=699.99,
                                  artist=artist_data_1,
                                  is_approved=True)
    return artist


@pytest.fixture
def auth_client():
    def func(user_instance=None):
        if user_instance is None:
            user_instance = User.objects.create_user(username='user', password='password', email='@email.com', bio='Bio')
        client = APIClient()
        instance, token = AuthToken.objects.create(user=user_instance)
        client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        return client
    return func
