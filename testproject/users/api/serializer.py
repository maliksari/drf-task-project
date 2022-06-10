from rest_framework import serializers
from ..models import CustomUser


class RegisterSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'password',)
        extra_kwargs = {
            'password': {'write_only': True}
        }
