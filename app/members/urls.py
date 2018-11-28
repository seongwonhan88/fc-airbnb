from django.urls import path, include
from . import apis
urlpatterns = [
    path('profile/<int:pk>/', apis.UserApiView.as_view(), name='user-profile'),
    path('facebook-auth-token/', apis.FacebookAuthTokenView.as_view(), name='facebook-auth'),
    path('saved/', apis.UserSavedView.as_view(), name='user-saved'),
    path('rest-auth/', include('rest_auth.urls')),
]
