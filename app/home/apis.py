from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics
from django_filters import rest_framework as filters

from home.filters import RoomFilter
from .serializers import RoomSerializer
from .models import Room


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
        room = Room.objects.prefetch_related('amenities').select_related('roominfo', 'hostimages').get(pk=pk)
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