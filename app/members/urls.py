from django.urls import path
from . import apis
urlpatterns = [
    path('profile/<int:pk>/', apis.UserApiView.as_view(), name='user-profile'),
    path('facebook-auth-token/', apis.FacebookAuthTokenView.as_view(), name='facebook-auth'),
    path('saved/', apis.UserSavedView.as_view(), name='user-saved'),
    path('save_room/', apis.UserRoomSaveView.as_view(), name='user-saveroom')
]
