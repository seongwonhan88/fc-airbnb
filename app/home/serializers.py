from rest_framework import serializers
from .models import Room, Amenity, RoomInfo, HostImages


class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = ('value',
                  'help_text',
                  'key'
        )


class RoomInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomInfo
        fields = (
            'room_info_1',
            'room_info_2',
            'room_info_3',
            'room_info_4',
            'room_info_5',
            'room_photo_1',
            'room_photo_2',
            'room_photo_3',
            'room_photo_4',
            'room_photo_5',
        )


class HostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostImages
        fields = (
            'host_thumbnail_url',
            'host_thumbnail_url_small',
        )


class RoomSerializer(serializers.ModelSerializer):
    host_images = HostImageSerializer()
    room_info = RoomInfoSerializer()
    amenities = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Room
        fields = ('pk',
                  'bathrooms',
                  'bedrooms',
                  'beds',
                  'person_capacity',
                  'room_name',
                  'room_type',
                  'room_and_property_type',
                  'public_address',
                  'city',
                  'price',
                  'lat',
                  'lng',
                  'created_at',
                  # 아래부터 외부모델 연결 필드 값
                  'amenities',
                  'room_info',
                  'host_images'
                  # 'host_thumbnails',
                  )
