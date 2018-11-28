from django.urls import path

from .apis import RoomListingApiView, RoomDetailApiView, RoomApiView

urlpatterns = [
    # path('listings/', RoomListingApiView.as_view(), name='room-list'),
    path('listings/<int:pk>/', RoomDetailApiView.as_view(), name='room-detail'),
    path('listings/', RoomApiView.as_view(), name='room-list-generic'),
]