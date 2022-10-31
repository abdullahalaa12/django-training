import pytest

from django.shortcuts import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
def test_detail_get_returned_fields(auth_client, user_data_1):
    url = reverse('users:detail', kwargs={'pk': user_data_1.pk})

    client = auth_client(user_data_1)
    response = client.get(url)

    assert response.data == {'id': user_data_1.id, 'username': user_data_1.username,
                             'email': user_data_1.email, 'bio': user_data_1.bio, }


@pytest.mark.django_db
def test_detail_patch_authenticated(auth_client, user_data_1):
    url = reverse('users:detail', kwargs={'pk': user_data_1.pk})

    bio = 'updated_bio'
    client = auth_client(user_data_1)
    response = client.patch(url, {'bio': bio})

    assert response.status_code == 200
    assert response.data == {'id': user_data_1.id, 'username': user_data_1.username,
                             'email': user_data_1.email, 'bio': bio}


@pytest.mark.django_db
def test_detail_patch_non_authenticated(auth_client, user_data_1):
    url = reverse('users:detail', kwargs={'pk': user_data_1.pk})

    bio = 'updated_bio'
    client = auth_client()
    response = client.patch(url, {'bio': bio})

    assert response.status_code == 403


@pytest.mark.django_db
def test_detail_put_authenticated(auth_client, user_data_1):
    url = reverse('users:detail', kwargs={'pk': user_data_1.pk})

    username = 'updated_username'
    email = 'updated_email@gmail.com'
    bio = 'updated_bio'
    client = auth_client(user_data_1)
    response = client.put(url, {'username': username, 'email': email, 'bio': bio})

    assert response.status_code == 200
    assert response.data == {'id': user_data_1.id, 'username': username,
                             'email': email, 'bio': bio}


@pytest.mark.django_db
def test_detail_put_authenticated_missing_fields(auth_client, user_data_1):
    url = reverse('users:detail', kwargs={'pk': user_data_1.pk})

    client = auth_client(user_data_1)
    response = client.put(url)

    expected_error_msg = ['This field is required.']
    assert response.status_code == 400
    assert response.data == {'username': expected_error_msg,
                             'email': expected_error_msg,
                             'bio': expected_error_msg}


@pytest.mark.django_db
def test_detail_put_non_authenticated(auth_client, user_data_1):
    url = reverse('users:detail', kwargs={'pk': user_data_1.pk})

    username = 'updated_username'
    email = 'updated_email@gmail.com'
    bio = 'updated_bio'
    client = auth_client()
    response = client.put(url, {'username': username, 'email': email, 'bio': bio})

    assert response.status_code == 403
