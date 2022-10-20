from django.contrib import admin
from .models import Album

# Register your models here.

class AlbumAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified',)


admin.site.register(Album, AlbumAdmin)
