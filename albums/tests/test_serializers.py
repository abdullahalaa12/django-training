import pytest
from ..serializers import AlbumSerializer
from django.http import HttpRequest

@pytest.mark.django_db
class TestSerializer:

    def test_album_serialization(self, album_data_1):
        serializer = AlbumSerializer(album_data_1)

        assert set(serializer.data.keys()) == set(['id', 'artist', 'name', 'release_date', 'cost'])
        assert serializer.data['id'] == album_data_1.id
        assert serializer.data['artist']['id'] == album_data_1.artist.id

    def test_album_deserialization(self, album_data_1):
        request = HttpRequest()
        request.method = 'POST'
        request.user = album_data_1.artist.user

        data = {
            'name': album_data_1.name,
            'release_date': album_data_1.release_date,
            'cost': album_data_1.cost
        }
        serializer = AlbumSerializer(context={'request': request})
        instance = serializer.create(data)

        assert instance.artist == album_data_1.artist
        assert instance.name == album_data_1.name
        assert instance.release_date == album_data_1.release_date
        assert instance.cost == album_data_1.cost
