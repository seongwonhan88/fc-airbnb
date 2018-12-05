from django.urls import path

from .apis import RoomDetailApiView, RoomApiView, BookingAPIView

urlpatterns = [
    path('listings/<int:pk>/', RoomDetailApiView.as_view(), name='room-detail'),
    path('listings/', RoomApiView.as_view(), name='room-list-generic'),
    path('booking/', BookingAPIView.as_view(), name='booking'),
    path('booking/<int:booking_id>/', BookingAPIView.as_view(), name='booking-del'),
]