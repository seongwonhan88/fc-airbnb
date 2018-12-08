from django.contrib.auth import get_user_model
from rest_framework import serializers

from home.serializers import RoomSerializer

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'date_joined',
            'img_profile',
            'id',
            'last_login',
            'saved_room',
        )


class HostUserSerializer(UserSerializer):
    listings = RoomSerializer()

    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + (
            'is_host',
            'listings',
            'rating',
        )
