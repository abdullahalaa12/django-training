from django.contrib import admin
from .models import Album


class AlbumAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified',)


admin.site.register(Album, AlbumAdmin)
