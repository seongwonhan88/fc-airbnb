from django.urls import path

from home.average import CityAveragePriceAPIView
from .apis import RoomDetailApiView, RoomApiView, BookingAPIView, BookingCancelAPIView, \
    UserReviewListAPIView, RoomReviewListAPIView, AmenityAPIView, RoomListingApiView, ReviewCreateListAPIView, \
    ReviewDelPatchAPIView, ReceiptAPIView

urlpatterns = [
    path('rooms/', RoomListingApiView.as_view()),
    path('listings/<int:pk>/', RoomDetailApiView.as_view(), name='room-detail'),
    path('listings/', RoomApiView.as_view(), name='room-list-generic'),
    path('booking/', BookingAPIView.as_view(), name='booking'),
    path('booking_cancel/', BookingCancelAPIView.as_view(), name='booking-cancel'),
    path('review/user/list/', UserReviewListAPIView.as_view(), name='review-user-list'),
    path('review/room/list/', RoomReviewListAPIView.as_view(), name='review-room-list'),
    path('review/<int:room_id>/', ReviewCreateListAPIView.as_view(), name='review-create'),
    path('review/del-patch/', ReviewDelPatchAPIView.as_view(), name='review-del-patch'),
    path('amenities/', AmenityAPIView.as_view(), name='amenity-view'),
    path('average/', CityAveragePriceAPIView.as_view(), name='average'),
    path('receipt/<int:pk>/', ReceiptAPIView.as_view(), name='receipt'),
]
