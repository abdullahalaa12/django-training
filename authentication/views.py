from django.views import View
from knox.views import LoginView as KnoxLoginView

from rest_framework.authentication import BasicAuthentication
from users.serializers import UserSerializer as DefaultUserSerializer

# Create your views here.


class Register(View):
    pass


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
