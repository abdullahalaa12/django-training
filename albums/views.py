from django.urls import reverse
from django.views.generic import CreateView
from .forms import AlbumForm

from .models import Album


# Create your views here.


class Create(CreateView):
    template_name = 'albums/create.html'
    form_class = AlbumForm

    def get_success_url(self):
        return reverse('artists:index')
