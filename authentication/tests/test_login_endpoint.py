import pytest
import base64
from django.shortcuts import reverse
from knox.models import AuthToken


def encode_to_base64(username, password):
    cred = username + ':' + password
    encoded_cred = base64.b64encode(cred.encode()).decode()
    return encoded_cred


@pytest.mark.django_db
class TestLogin:
    url = reverse('authentication:login')

    def test_login_missing_credentials(self, auth_client):
        client = auth_client()
        response = client.post(self.url)

        assert response.status_code == 401
        assert response.data['detail'] == 'Authentication credentials were not provided.'

    def test_login_invalid_credentials(self, auth_client):
        encoded_cred = encode_to_base64('invalid_username', 'invalid_password')

        client = auth_client()
        client.credentials(HTTP_AUTHORIZATION='Basic ' + encoded_cred)
        response = client.post(self.url)

        assert response.status_code == 401
        assert response.data['detail'] == 'Invalid username/password.'

    def test_login_valid_credentials(self, auth_client, user_data_1):
        encoded_cred = encode_to_base64(user_data_1.username, '123')

        client = auth_client()
        client.credentials(HTTP_AUTHORIZATION='Basic ' + encoded_cred)
        response = client.post(self.url)

        assert response.status_code == 200
        assert response.data['token'].startswith(AuthToken.objects.get(user=user_data_1).token_key)
        assert response.data['user'] == {'id': user_data_1.id, 'username': user_data_1.username,
                                         'email': user_data_1.email, 'bio': user_data_1.bio}
