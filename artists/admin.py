from django.contrib import admin
from .models import Artist


@admin.display(description='# Approved Albums')
def approved_albums_count(obj):
    return obj.album_set.filter(is_approved=True).count()


class ArtistAdmin(admin.ModelAdmin):
    list_display = ('stage_name', approved_albums_count)


admin.site.register(Artist, ArtistAdmin)
