from django.contrib.auth import get_user_model
from django.db import models
from members.models import NormalUser, HostUser

User = get_user_model()


class Room(models.Model):
    bathrooms = models.IntegerField()
    bedrooms = models.IntegerField()
    beds = models.IntegerField()
    person_capacity = models.IntegerField()
    room_name = models.CharField(max_length=100)
    room_type = models.CharField(max_length=20)
    # 디테일 화면에서 이름 위에 표시되는 이름 (예. 공동주택의 개인실)
    room_and_property_type = models.CharField(max_length=20)
    public_address = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    price = models.IntegerField()
    lat = models.FloatField()
    lng = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    room_info_1 = models.TextField()
    room_info_2 = models.TextField()
    room_info_3 = models.TextField()
    room_info_4 = models.TextField()
    # 확장되는 모델 필드들
    amenities = models.ManyToManyField('Amenity')
    bookings = models.ManyToManyField(NormalUser, through='Booking')
    room_host = models.ForeignKey(HostUser, on_delete=models.CASCADE, related_name='listed_room')

    def __str__(self):
        return self.room_name


class Amenity(models.Model):
    value = models.CharField(max_length=50)
    help_text = models.CharField(max_length=100)
    key = models.CharField(max_length=50)

    def __str__(self):
        return self.key


class RoomPhoto(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_photos')
    room_photo = models.ImageField(upload_to='picture/host/listing/')


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='booking_info')
    guest = models.ForeignKey(NormalUser, on_delete=models.CASCADE)
    num_guest = models.IntegerField()
    # 실제 머무른 기간
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    # 예약을 신청한 기간
    created_date = models.DateTimeField(auto_now_add=True)


class BookingDates(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='reserved_dates')
    reserved_date = models.DateField()


class HostImages(models.Model):
    host_images = models.OneToOneField(Room, on_delete=models.CASCADE, primary_key=True)
    host_thumbnail_url = models.ImageField(upload_to='pictures/host/', blank=True, null=True)
    host_thumbnail_url_small = models.ImageField(upload_to='pictures/host/', blank=True, null=True)


class Review(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    guest = models.ForeignKey(NormalUser, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
