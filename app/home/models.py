from django.contrib.auth import get_user_model
from django.db import models

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

    amenities = models.ManyToManyField('Amenity')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.room_name



class Amenity(models.Model):
    value = models.CharField(max_length=50)
    help_text = models.CharField(max_length=100)
    key = models.CharField(max_length=50)

    def __str__(self):
        return self.key


class HouseInfo(models.Model):
    # One To One 모델로 바꾸기
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_info')
    # 숙소하이라이트 부분
    home_info_1 = models.TextField()
    # 기본 설명
    home_info_2 = models.TextField()
    # 자세히 알아보기 추가 내용
    home_info_3 = models.TextField()
    # 편의시설
    home_info_4 = models.TextField()
    # 편의시설 모두 보기
    home_info_5 = models.TextField()
    # 관련 사진들
    photo1 = models.ImageField(upload_to='picture/host/listing/')
    photo2 = models.ImageField(upload_to='picture/host/listing/')
    photo3 = models.ImageField(upload_to='picture/host/listing/')
    photo4 = models.ImageField(upload_to='picture/host/listing/')
    photo5 = models.ImageField(upload_to='picture/host/listing/')


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE,related_name='booking_info')
    guest = models.ForeignKey(User, on_delete=models.CASCADE)
    num_guest = models.IntegerField()
    # 실제 머무른 기간
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    # 예약을 신청한 기간
    reserved_date = models.DateTimeField(auto_now_add=True)


class HostThumbnailImg(models.Model):
    # one-to-one 모델로 room과 연결
    room = models.OneToOneField(Room, on_delete=models.CASCADE, related_name='host_thumbnails')
    host_thumbnail_url = models.ImageField(upload_to='pictures/host/', blank=True, null=True)
    host_thumbnail_url_small = models.ImageField(upload_to='pictures/host/', blank=True, null=True)
