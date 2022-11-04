from rest_framework import generics, pagination


class AlbumPagination(pagination.LimitOffsetPagination):
    default_limit = 10
