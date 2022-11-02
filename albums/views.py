from rest_framework import generics, pagination

from .models import Album
from .serializers import AlbumSerializer
from .permissions import IsArtistOrReadOnly


class AlbumPagination(pagination.LimitOffsetPagination):
    default_limit = 10


class Index(generics.ListCreateAPIView):
    queryset = Album.approved_albums.all()
    serializer_class = AlbumSerializer
    permission_classes = [IsArtistOrReadOnly, ]
    pagination_class = AlbumPagination
