from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime

from artists.models import Artist

# Create your views here.


def create(request):
    if request.method == 'GET':
        return render(request, 'albums/create.html', {'artists_list': Artist.objects.all()})

    artist_id = request.POST['artist']
    name = request.POST['name']
    release_date = request.POST['release_date']
    cost = request.POST['cost']
    print(release_date)
    try:
        artist = Artist.objects.get(pk=artist_id)
        artist.album_set.create(name=name, release_date=datetime.strptime(release_date, '%Y-%m-%dT%H:%M'), cost=cost)
        return HttpResponseRedirect(reverse('artists:index'))

    except Exception as e:
        return render(request, 'albums/create.html', {'artists_list': Artist.objects.all(), 'error_msg': str(e)})
