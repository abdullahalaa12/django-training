from django.urls import reverse
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Artist


class Index(ListView):
    queryset = Artist.objects.prefetch_related('album_set')
    context_object_name = 'artists_list'
    template_name = 'artists/index.html'


class Create(LoginRequiredMixin, CreateView):
    model = Artist
    fields = ['stage_name', 'social_link']
    template_name = 'artists/create.html'

    def get_success_url(self):
        return reverse('artists:index')
