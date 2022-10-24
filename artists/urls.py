from django.urls import path
from . import views

app_name = 'artists'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('create', views.Create.as_view(), name='create'),
]