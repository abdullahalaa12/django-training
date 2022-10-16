from django.shortcuts import render
from .models import Artist

# Create your views here.

def index(request):
    artists_list = Artist.objects.all()
    context = {'artists_list': artists_list}
    return render(request, 'artists/index.html', context)