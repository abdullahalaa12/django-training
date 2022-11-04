import pytest
from django.shortcuts import reverse
from knox.models import AuthToken


@pytest.mark.django_db
class TestLogout:
    url = reverse('authentication:logout')

    def test_logout(self, auth_client, user_data_1):
        client = auth_client(user_data_1)
        response = client.post(self.url)

        assert response.status_code == 204
        assert AuthToken.objects.filter(user=user_data_1).count() == 0
