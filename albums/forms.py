from django.forms import ModelForm
from django import forms
from .models import Album


class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'


class AlbumForm(ModelForm):

    class Meta:
        model = Album
        fields = ['artist', 'name', 'release_date', 'cost']
        widgets = {
            'release_date': DateTimeInput(),
        }
