from django.contrib import admin
from .models import Artist
from albums.models import Album


@admin.display(description='# Approved Albums')
def approved_albums_count(obj):
    return obj.album_set.filter(is_approved=True).count()


class AlbumInline(admin.TabularInline):
    model = Album


class ArtistAdmin(admin.ModelAdmin):
    list_display = ('stage_name', approved_albums_count)
    inlines = [AlbumInline, ]


admin.site.register(Artist, ArtistAdmin)
