import logging
from rest_framework import serializers

from .models import User
from core.models import Interview

logger = logging.getLogger(__name__)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'password', 'is_staff']
        extra_kwargs = {'password': {'write_only': True}, 'id': {'read_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data['username'] = validated_data['email']
        user = User(**validated_data)
        Interview.objects.get_or_create(candidate=user)
        user.set_password(password)
        user.save()
        return user

    @staticmethod
    def remove_fields(validated_data, field):
        return validated_data.pop(field)
