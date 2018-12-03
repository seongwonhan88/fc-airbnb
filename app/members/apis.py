from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from home.models import Room
from home.serializers import RoomSerializer
from .permissions import BearerAuthentication, IsOwner
from .serializers import UserSerializer


User = get_user_model()


class UserApiView(APIView):
    # 인증 및 권한은 front/ios에서 token 정리가 되면 해제
    # permission_classes = (permissions.IsAuthenticated,)
    # authentication_classes = (BearerAuthentication,)
    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class AuthTokenView(APIView):

    def post(self, request):
        user_id = request.data.get('user_id')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')

        if User.objects.filter(username=user_id).exists():
            user = User.objects.get(username=user_id)
        else:
            user = User.objects.create_user(username=user_id, first_name=first_name, last_name=last_name, email=email)
        token = Token.objects.get_or_create(user=user)[0]
        data = {
            'token': token.key,
            'user': UserSerializer(user).data
        }
        return Response(data)


class UserSavedView(APIView):
    authentication_classes = (BearerAuthentication,)
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def get(self, request):
        """
        사용자가 'saved'한 숙소들을 보여줌, saved_room 의 related_name은 saved_user로 주었음
        :param request:
        :return:
        """
        room = Room.objects.prefetch_related('saved_user').filter(saved_user=request.user)
        serializer = RoomSerializer(room, many=True)
        return Response(serializer.data)


class UserRoomSaveView(APIView):
    authentication_classes = (BearerAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        """
        Token을 소유한 사용자가 해당 방의 pk를 전달하면 사용자의 'saved'목록에 추가
        이미 추가된 방이면 400 bad request를 돌려주면서 메지시 전달
        :param request: room_id 값을 param으로 전달
        :return:
        """
        user = User.objects.get(username=request.user)
        room = Room.objects.get(pk=request.data.get('room_id'))
        if room.saved_user.filter(username=user).exists():
            content = {'redundancy': 'already saved this room'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        else:
            user.saved_room.add(room)
            content = {'message': 'successfully saved'}
        return Response(content, status=status.HTTP_201_CREATED)

    def delete(self, request):
        """
        Token 소유자가 이미 'saved'처리 된 방을 목록에서 제거하고 싶을 때 요청
        :param request: room_id 값을 param으로 전달
        :return: room_id에 해당하는 내용 제거
        """
        user = User.objects.get(username=request.user)
        room = Room.objects.get(pk=request.data.get('room_id'))
        if room.saved_user.filter(username=user).exists():
            user.saved_room.remove(room)
            content = {'message': 'successfully removed'}
            return Response(content, status=status.HTTP_200_OK)
        else:
            content = {'message': 'room is already removed'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)