from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from home.models import Room
from home.serializers import RoomSerializer
from .permissions import BearerAuthentication
from .serializers import UserSerializer


User = get_user_model()


class UserApiView(APIView):
    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class FacebookAuthTokenView(APIView):

    def post(self, request):
        facebook_id = request.data.get('user_id')

        if User.objects.filter(username=facebook_id).exists():
            user = User.objects.get(username=facebook_id)
        else:
            user = User.objects.create_user(username=facebook_id)
        token = Token.objects.get_or_create(user=user)[0]
        data = {
            'token': token.key,
            'user': UserSerializer(user).data
        }
        return Response(data)


class UserSavedView(APIView):
    authentication_classes = (BearerAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        """
        사용자가 'saved'한 숙소들을 보여줌, saved_room 의 related_name은 saved_user로 주었음
        :param request:
        :return:
        """
        room = Room.objects.get(saved_user=request.user)
        serializer = RoomSerializer(room)
        return Response(serializer.data)