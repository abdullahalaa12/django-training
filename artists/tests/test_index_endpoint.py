import pytest
from django.shortcuts import reverse


@pytest.mark.django_db
class TestIndex:
    url = reverse('artists:index')

    def test_list(self, auth_client, artist_data_1):
        client = auth_client()
        response = client.get(self.url)

        assert response.status_code == 200
        assert response.data == [
            {'id': artist_data_1.id, 'stage_name': artist_data_1.stage_name, 'social_link': artist_data_1.social_link}
        ]

    def test_post_missing_field(self, auth_client):
        client = auth_client()
        response = client.post(self.url)
        expected_error_msg = ['This field is required.']

        assert response.status_code == 400
        assert response.data == {'stage_name': expected_error_msg}

    def test_post_non_unique_stage_name(self, auth_client, artist_data_1):
        client = auth_client()
        response = client.post(self.url, {'stage_name': artist_data_1.stage_name})

        assert response.status_code == 400
        assert response.data['stage_name'][0].code == 'unique'

    def test_post_valid_data(self, auth_client):
        stage_name = 'Michael Jackson'
        social_link = 'https://twitter.com/michaeljackson'

        client = auth_client()
        response = client.post(self.url, {'stage_name': stage_name, 'social_link': social_link})

        assert response.status_code == 201
        assert response.data == {'id': 1, 'stage_name': stage_name, 'social_link': social_link}
