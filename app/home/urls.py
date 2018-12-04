from django.urls import path

from .apis import RoomDetailApiView, RoomApiView, BookingAPIView, BookingCancelAPIView

urlpatterns = [
    path('listings/<int:pk>/', RoomDetailApiView.as_view(), name='room-detail'),
    path('listings/', RoomApiView.as_view(), name='room-list-generic'),
    path('booking/', BookingAPIView.as_view(), name='booking'),
    path('booking_cancel/', BookingCancelAPIView.as_view(), name='booking-cancel'),

]
