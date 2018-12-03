from rest_framework import serializers
from .models import Room, Amenity, RoomInfo, HostImages, Booking, BookingDate


class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = ('value',
                  'help_text',
                  )


class RoomInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomInfo
        fields = (
            'room_info_1',
            'room_info_2',
            'room_info_3',
            'room_info_4',
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


class BookingDateSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookingDate
        fields = (
            'reserved_date',
        )


class BookingSerializer(serializers.ModelSerializer):
    reserved_dates = BookingDateSerializer(many=True, read_only=True)

    class Meta:
        model = Booking
        fields = (
            'id',
            'room',
            'guest',
            'num_guest',
            'check_in_date',
            'check_out_date',
            'reserved_dates',
        )


class RoomSerializer(serializers.ModelSerializer):
    hostimages = HostImageSerializer()
    roominfo = RoomInfoSerializer()
    amenities = serializers.StringRelatedField(many=True, read_only=True)
    booking_info = BookingSerializer(many=True)


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
                  'roominfo',
                  'hostimages',
                  'booking_info',
                  )
        read_only_fields = (
            'roominfo',
            'hostimages',
            'booking_info',
        )
