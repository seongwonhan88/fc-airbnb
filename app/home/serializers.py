import datetime
from rest_framework import serializers
from .models import Room, Amenity, HostImages, Booking, Review


class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = ('value',
                  'help_text',
                  )


class HostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostImages
        fields = (
            'host_thumbnail_url',
            'host_thumbnail_url_small',
        )


class BookingDateRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        return value.reserved_date


class BookingSerializer(serializers.ModelSerializer):
    reserved_dates = BookingDateRelatedField(many=True, read_only=True)

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
    amenities = serializers.StringRelatedField(many=True, read_only=True)
    room_photo = serializers.SerializerMethodField()

    def get_room_photo(self, obj):
        return obj.room_photos.values_list('room_photo', flat=True)

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
                  'room_info_1',
                  'room_info_2',
                  'room_info_3',
                  'room_info_4',
                  'created_at',
                  # 아래부터 외부모델 연결 필드 값
                  'amenities',
                  'hostimages',
                  'room_photo',
                  )
        read_only_fields = (
            'hostimages',
            'booking_info',
        )


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = (
            'room',
            'guest',
            'comment',
            'created_at',
        )
