import pytest

from django.shortcuts import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
class TestRegister:
    url = reverse('authentication:register')

    def test_register_post_missing_fields(self, auth_client):
        client = auth_client()
        response = client.post(self.url)
        expected_error_msg = ['This field is required.']

        assert response.status_code == 400
        assert response.data == {'username': expected_error_msg,
                                 'email': expected_error_msg,
                                 'password1': expected_error_msg,
                                 'password2': expected_error_msg}

    def test_register_post_non_unique_username(self, auth_client, user_data_1):
        client = auth_client()
        response = client.post(self.url, {'username': user_data_1.username})

        assert response.status_code == 400
        assert response.data['username'][0].code == 'unique'

    def test_register_post_no_passwords_match(self, auth_client):
        client = auth_client()
        response = client.post(self.url, {'username': 'abdullah', 'email': 'a@email.com', 'password1': '123',
                                          'password2': '12'})

        assert response.status_code == 400
        assert response.data[0] == "password1 doesn't match password2"

    def test_register_post_password_strength(self, auth_client):
        client = auth_client()
        response = client.post(self.url, {'username': 'abdullah', 'email': 'a@email.com', 'password1': '123',
                                          'password2': '123'})

        assert response.status_code == 400
        assert response.data[0].code == 'invalid'

    def test_register_post_success(self, auth_client):
        client = auth_client()
        response = client.post(self.url, {'username': 'abdullah', 'email': 'a@email.com', 'password1': 'Aa123456123456',
                                          'password2': 'Aa123456123456'})

        assert response.status_code == 201
