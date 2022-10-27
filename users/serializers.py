from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

from .models import User


class UserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    email = serializers.CharField(required=True)

    def create(self, validated_data):
        if validated_data["password1"] != validated_data["password2"]:
            raise serializers.ValidationError("password1 doesn't match password2")

        try:
            validate_password(validated_data["password1"])
        except Exception as e:
            raise serializers.ValidationError(e)

        return User.objects.create_user(username=validated_data["username"],
                                        email=validated_data.get("email"),
                                        password=validated_data["password1"])

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'password1', 'password2']
