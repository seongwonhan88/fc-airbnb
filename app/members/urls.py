from django.urls import path
from . import apis
urlpatterns = [
    path('profile/<int:pk>/', apis.UserApiView.as_view(), name='user-profile'),
]
