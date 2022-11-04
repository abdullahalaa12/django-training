from rest_framework import permissions
from artists.models import Artist


class IsArtistOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS or
            request.user and
            request.user.is_authenticated and
            Artist.objects.filter(user=request.user).exists()
        )
