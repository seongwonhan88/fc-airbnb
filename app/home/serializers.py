import datetime

from django.utils.timezone import now
from rest_framework import serializers

from .models import Room, Amenity, RoomInfo, HostImages, Booking, BookingDates


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


class BookingDatesSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookingDates
        fields = (
            'reserved_date',
        )


class BookingSerializer(serializers.ModelSerializer):
    reserved_dates = BookingDatesSerializer(many=True, read_only=True)

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

    def validate(self, data):
        # 예약 요청 정보
        chi = data['check_in_date']
        cho = data['check_out_date']
        now = datetime.date.today()
        guest = data['num_guest']

        # 비교 대상
        room = Room.objects.get(room_name=data['room'])
        room_id = room.id
        room_capacity = room.person_capacity

        if chi < now:
            raise ValueError('오늘보다 이전 날을 선택할 수 없습니다')

        if chi > cho or chi == cho:
            raise ValueError('예약 날짜가 맞지 않습니다')

        if guest > room_capacity:
            raise ValueError(f'{room_capacity}명 이하로 입력해주세요')

        if guest <= 0:
            raise ValueError('한 명 이상 예약해주세요')

        return data


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