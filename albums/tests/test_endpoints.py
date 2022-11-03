import pytest
from django.shortcuts import reverse
from django.utils import timezone
from ..serializers import AlbumSerializer, Album


@pytest.mark.django_db
class TestIndex:
    url = reverse('albums:index')

    def test_index_uses_expected_serializer(self, auth_client, album_data_1):
        client = auth_client()
        response = client.get(self.url)

        assert response.data['results'] == AlbumSerializer(Album.objects.all(), many=True).data

    def test_index_get(self, auth_client):
        client = auth_client()
        response = client.get(self.url)

        assert response.status_code == 200

    def test_index_post_permitted(self, auth_client, album_data_1):
        client = auth_client(album_data_1.artist.user)
        response = client.post(self.url, {'release_date': timezone.now(), 'cost': '199.99'})

        assert response.status_code == 201

    def test_index_post_unpermitted(self, auth_client, album_data_1):
        client = auth_client()
        response = client.post(self.url, {'release_date': timezone.now(), 'cost': '199.99'})

        assert response.status_code == 403
