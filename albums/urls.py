from django.urls import path
from . import views

app_name = 'albums'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('filter/', views.Filter.as_view(), name='filter')
]
