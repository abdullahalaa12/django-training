from rest_framework import generics

from .models import Album
from .serializers import AlbumSerializer
from .permissions import IsArtistOrReadOnly


class Index(generics.ListCreateAPIView):
    queryset = Album.approved_albums.all()
    serializer_class = AlbumSerializer
    permission_classes = [IsArtistOrReadOnly, ]
