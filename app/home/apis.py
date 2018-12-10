import datetime
from django_filters import rest_framework as filters
from rest_framework import status, generics, permissions, serializers
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from members.permissions import BearerAuthentication, IsOwner
from .filters import RoomFilter
from .models import Room, Booking, Review, Amenity
from .serializers import RoomSerializer, BookingSerializer, ReviewSerializer, AmenitySerializer


class AmenityAPIView(generics.ListAPIView):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer


class RoomListingApiView(APIView):

    def get(self, request, format=None):
        room = Room.objects.all().prefetch_related('amenities', 'room_photos').select_related('hostimages', 'room_host')
        serializer = RoomSerializer(room, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoomDetailApiView(APIView):
    """
    기본 페이지 구성을 위해 get 요청 시 전체 숙소 목록을 return
    """
    def get(self, request, pk, format=None):
        room = Room.objects.prefetch_related('amenities', 'booking_info').select_related('hostimages', 'room_host', 'room_photos').get(pk=pk)
        serializer = RoomSerializer(room)
        return Response(serializer.data)


class RoomApiView(generics.ListAPIView):
    """
    query필터 사용을 위해 djang-filter를 pip로 설치.
    해당 뷰를 사용하면 url param값에 주는 조건대로 검색이 가능
    filter_class 에는 customize 한 필터들을 적용
    """
    queryset = Room.objects.all().prefetch_related('amenities', 'booking_info', 'room_photos', 'room_host').select_related('hostimages')
    serializer_class = RoomSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = RoomFilter


class BookingAPIView(APIView):
    """
    예약 APIView, get 요청 시 user_id를 받아서
    """
    authentication_classes = (BearerAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        user = request.auth.user_id
        reserved_room = Booking.objects.filter(guest_id=user).prefetch_related('reserved_dates')
        serializer = BookingSerializer(reserved_room, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        user = request.auth.user_id
        serializer = BookingSerializer(data={**request.data, 'guest': user}, )
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


class BookingCancelAPIView(APIView):
    """
    예약을 생성한 사용자일 경우에만 취소 가능한 APIView
    """
    authentication_classes = (BearerAuthentication,)
    permission_classes = (IsOwner,)

    def delete(self, request):
        booking = get_object_or_404(Booking, id=request.data.get('booking_id'), guest=request.user)
        booking.delete()
        context = {
            "message": "정상적으로 예약이 취소됐습니다."
        }
        return Response(context, status=status.HTTP_204_NO_CONTENT)


class RoomReviewListAPIView(APIView):
    # 해당 집 모든 후기 목
    def get(self, request):
        review = Review.objects.filter(room_id=request.data.get('review_id'))
        serializer = ReviewSerializer(review, many=True)
        return Response(serializer.data)


class UserReviewListAPIView(APIView):
    # 로그인 유저가 작성한 후기 목록을 보여줌
    authentication_classes = (BearerAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = request.auth.user_id
        review = Review.objects.filter(guest_id=user)
        serializer = ReviewSerializer(review, many=True)
        return Response(serializer.data)


class ReviewAPIView(APIView):
    authentication_classes = (BearerAuthentication,)
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwner,
    )

    def post(self, request, room_id):
        user = request.auth.user_id
        serializer = ReviewSerializer(data={**request.data, 'guest': user, 'room': room_id}, )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, room_id):
        # pk = request.data.get('pk')
        if not room_id:
            raise serializers.ValidationError({"detail": "pk가 전송되지 않았습니다."})
        review = get_object_or_404(Review, pk=room_id)
        review.delete()
        context = {
            "message": "후기를 삭제했습니다."
        }
        return Response(context, status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, room_id):
        review = Review.objects.get(pk=room_id)
        if not room_id:
            raise serializers.ValidationError({"detail": "해당 Review가 없습니다"})
        serializer = ReviewSerializer(review, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)