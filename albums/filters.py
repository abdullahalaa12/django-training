from django_filters import rest_framework as filters

from .models import Album


class AlbumFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')

    cost__gte = filters.NumberFilter(field_name='cost', lookup_expr='gte')
    cost__lte = filters.NumberFilter(field_name='cost', lookup_expr='lte')

    class Meta:
        model = Album
        fields = ['name', 'cost']
