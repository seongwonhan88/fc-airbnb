from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

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
