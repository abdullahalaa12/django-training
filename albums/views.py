from rest_framework import generics, pagination
from django_filters import rest_framework as filters

from .models import Album
from .serializers import AlbumSerializer
from .permissions import IsArtistOrReadOnly
from .filters import AlbumFilter


class AlbumPagination(pagination.LimitOffsetPagination):
    default_limit = 10


class Index(generics.ListCreateAPIView):
    queryset = Album.approved_albums.all()
    serializer_class = AlbumSerializer
    permission_classes = [IsArtistOrReadOnly, ]
    pagination_class = AlbumPagination

    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = AlbumFilter
