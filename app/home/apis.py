import datetime

from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics, permissions
from django_filters import rest_framework as filters

from members.permissions import BearerAuthentication
from .serializers import RoomSerializer, BookingSerializer, BookingDateSerializer
from .models import Room, BookingDate, Booking
from home.filters import RoomFilter


class RoomListingApiView(APIView):

    def get(self, request, format=None):
        room = Room.objects.all().prefetch_related('amenities').select_related('roominfo', 'hostimages')
        serializer = RoomSerializer(room, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoomDetailApiView(APIView):

    def get(self, request, pk, format=None):
        room = Room.objects.prefetch_related('amenities', 'booking_info').select_related('roominfo', 'hostimages').get(pk=pk)
        serializer = RoomSerializer(room)
        return Response(serializer.data)


class RoomApiView(generics.ListAPIView):
    """
    query필터 사용을 위해 djang-filter를 pip로 설치.
    해당 뷰를 사용하면 url param값에 주는 조건대로 검색이 가능
    """
    queryset = Room.objects.all().prefetch_related('amenities').select_related('roominfo', 'hostimages')
    serializer_class = RoomSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = RoomFilter


class BookingAPIView(APIView):
    authentication_classes = (
        BearerAuthentication,
    )
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def get(self, request, format=None):
        user = request.auth.user_id
        reserved_room = Booking.objects.filter(guest_id=user).prefetch_related('reserved_dates')
        serializer = BookingSerializer(reserved_room, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        user = request.auth.user_id
        serializer = BookingSerializer(data={**request.data, 'guest': user},)
        if serializer.is_valid():
            serializer.save()

            booking = Booking.objects.last()
            chi = booking.check_in_date
            cho = booking.check_out_date
            delta = cho - chi
            days = delta.days
            for i in range(1, days):
                day = datetime.timedelta(i)
                date = booking.check_in_date + day
                booking.reserved_dates.create(reserved_date=date)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        booking = get_object_or_404(Booking, id=request.data.get('booking_id'), guest=request.user)
        booking.delete()
        content = {
            "message": "정상적으로 예약이 취소됐습니다."
        }
        return Response(content, status=status.HTTP_204_NO_CONTENT)


class BookingDateAPIView(APIView):
    authentication_classes = (
        BearerAuthentication,
    )
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def get(self, request, pk,format=None):
        bookingdate = BookingDate.objects.filter(booking__id=pk)
        serializer = BookingDateSerializer(bookingdate, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
