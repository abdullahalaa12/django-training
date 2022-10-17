from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Artist


# Create your views here.

def index(request):
    artists_list = Artist.objects.all()
    context = {'artists_list': artists_list}
    return render(request, 'artists/index.html', context)


def create(request):
    if request.method == 'GET':
        return render(request, 'artists/create.html')

    stage_name = request.POST['stage_name']
    social_link = request.POST['social_link']

    try:
        Artist.objects.create(stage_name=stage_name, social_link=social_link)
        return HttpResponseRedirect(reverse('artists:index'))
    except Exception as e:
        return render(request, 'artists/create.html', {'error_msg': str(e)})
