from rest_framework import serializers
from .models import Room, Amenity, HouseInfo, HostThumbnailImg


class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = ('value',
                  'help_text',
                  'key'
        )


class HouseInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseInfo
        fields = (
            'home_info_1',
            'home_info_2',
            'home_info_3',
            'home_info_4',
            'home_info_5',
            'photo1',
            'photo2',
            'photo3',
            'photo4',
            'photo5',
        )


class HostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostThumbnailImg
        fields = (
            'host_thumbnail_url',
            'host_thumbnail_url_small',
        )


class RoomSerializer(serializers.ModelSerializer):
    room_info = serializers.StringRelatedField(many=True, read_only=True)
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
                  # 'host_thumbnails',
                  )
