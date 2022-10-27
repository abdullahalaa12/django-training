from rest_framework import generics
from knox.views import LoginView as KnoxLoginView

from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from users.serializers import UserSerializer as DefaultUserSerializer

# Create your views here.


class Register(generics.CreateAPIView):
    model = get_user_model()
    permission_classes = [AllowAny, ]
    serializer_class = DefaultUserSerializer


class Login(KnoxLoginView):
    authentication_classes = [BasicAuthentication, ]

    def get_post_response_data(self, request, token, instance):
        UserSerializer = DefaultUserSerializer

        data = {
            'token': token
        }
        if UserSerializer is not None:
            data["user"] = UserSerializer(
                request.user,
                context=self.get_context()
            ).data
        return data
