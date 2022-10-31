from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('<int:pk>', views.UserDetail.as_view(), name='detail'),
]
