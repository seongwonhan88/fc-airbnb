from django.urls import path
from . import apis
urlpatterns = [
    path('profile/<int:pk>/', apis.UserApiView.as_view(), name='user-profile'),
    path('auth-token/', apis.AuthTokenView.as_view(), name='auth-token'),
    path('saved/', apis.UserSavedView.as_view(), name='user-saved'),
    path('save_room/', apis.UserRoomSaveView.as_view(), name='user-saveroom'),
    path('room_create/', apis.RoomCreateAPIView.as_view(), name='room-create'),
    path('room_photo_upload/', apis.RoomPhotoUploadAPIView.as_view(), name='photo-upload'),
    path('upload/', apis.RoomPhotoSerializerUploadAPIView.as_view(), name='photo-serializer'),
]