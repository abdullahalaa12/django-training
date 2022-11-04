from rest_framework import generics
from rest_framework.exceptions import ValidationError
from django_filters import rest_framework as filters

from .models import Album
from .serializers import AlbumSerializer
from .permissions import IsArtistOrReadOnly
from .filters import AlbumFilter
from .paginations import AlbumPagination


class Index(generics.ListCreateAPIView):
    queryset = Album.approved_albums.all()
    serializer_class = AlbumSerializer
    permission_classes = [IsArtistOrReadOnly, ]
    pagination_class = AlbumPagination

    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = AlbumFilter


class Filter(generics.ListAPIView):
    serializer_class = AlbumSerializer
    pagination_class = AlbumPagination

    def get_queryset(self):
        queryset = Album.approved_albums.all()
        params = self.request.query_params

        name, cost__gte, cost__lte = params.get('name'), params.get('cost__gte'), params.get('cost__lte')
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        try:
            if cost__gte is not None:
                queryset = queryset.filter(cost__gte=cost__gte)
            if cost__lte is not None:
                queryset = queryset.filter(cost__lte=cost__lte)
        except Exception:
            raise ValidationError({"cost": "enter a number"})
        return queryset
