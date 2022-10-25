from .models import Artist

from .serializers import ArtistSerializer
from rest_framework import generics


class Index(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
