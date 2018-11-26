from django.urls import path
from . import apis
urlpatterns = [
    path('profile/<int:pk>/', apis.UserApiView.as_view(), name='user-profile'),
    path('facebook-auth-token/', apis.FacebookAuthTokenView.as_view(), name='facebook-auth')
]
