from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', ]
        extra_kwargs = {'username': {'required': True, 'allow_blank': False},
                        'email': {'required': True, 'allow_blank': False},
                        'bio': {'required': True, 'allow_blank': False}}
