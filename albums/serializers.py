from rest_framework import serializers
from .models import Album
from artists.serializers import ArtistSerializer, Artist


class AlbumSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['artist'] = Artist.objects.get(user=user)
        return super(AlbumSerializer, self).create(validated_data)

    class Meta:
        model = Album
        fields = ['id', 'artist', 'name', 'release_date', 'cost']
