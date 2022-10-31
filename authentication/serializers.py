from rest_framework import serializers
from django.contrib.auth import get_user_model, password_validation

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def is_password_match(self, password1, password2):
        return password1 == password2

    def create(self, validated_data):
        if not self.is_password_match(validated_data["password1"], validated_data["password2"]):
            raise serializers.ValidationError("password1 doesn't match password2")

        try:
            password_validation.validate_password(validated_data["password1"])
        except Exception as e:
            raise serializers.ValidationError(e)

        return User.objects.create_user(username=validated_data["username"],
                                        email=validated_data.get("email"),
                                        password=validated_data["password1"])

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'password1', 'password2']
        extra_kwargs = {'email': {'required': True, 'allow_blank': False}}
