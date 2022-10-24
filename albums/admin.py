from django.contrib import admin
from django import forms
from django.forms.models import BaseInlineFormSet

from .models import Album, Song


class SongFormSet(BaseInlineFormSet):

    def clean(self):
        super(SongFormSet, self).clean()
        if any(self.errors):
            return
        if not any(cleaned_data and not cleaned_data.get('DELETE', False)
                   for cleaned_data in self.cleaned_data):
            raise forms.ValidationError('At least one item required.')


class SongInline(admin.TabularInline):
    model = Song
    formset = SongFormSet


class AlbumAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified',)
    inlines = [SongInline, ]


admin.site.register(Album, AlbumAdmin)
admin.site.register(Song)
