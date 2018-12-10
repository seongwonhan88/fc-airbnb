from django.urls import path
from .apis import RoomDetailApiView, RoomApiView, BookingAPIView, BookingCancelAPIView, ReviewAPIView, \
    UserReviewListAPIView, RoomReviewListAPIView, AmenityAPIView

urlpatterns = [
    path('listings/<int:pk>/', RoomDetailApiView.as_view(), name='room-detail'),
    path('listings/', RoomApiView.as_view(), name='room-list-generic'),
    path('booking/', BookingAPIView.as_view(), name='booking'),
    path('booking_cancel/', BookingCancelAPIView.as_view(), name='booking-cancel'),
    path('review/user/list/', UserReviewListAPIView.as_view(), name='review-user-list'),
    path('review/room/list/', RoomReviewListAPIView.as_view(), name='review-room-list'),
    path('review/<int:room_id>/', ReviewAPIView.as_view(), name='review'),
    path('amenities/', AmenityAPIView.as_view(), name='amenity-view'),
]
