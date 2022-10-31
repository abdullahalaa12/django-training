import pytest
from rest_framework.test import APIClient
from knox.models import AuthToken

from django.contrib.auth import get_user_model

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
def auth_client():
    def func(user_instance=None):
        if user_instance is None:
            user_instance = User.objects.create_user(username='user', password='password', email='@email.com', bio='Bio')
        client = APIClient()
        instance, token = AuthToken.objects.create(user=user_instance)
        client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        return client
    return func
