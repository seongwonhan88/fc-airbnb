from django.db import models

# Create your models here.
class Room(models.Model):
    ROOM_TYPES = (
        ('E','entire'),
        ('P','private'),
        ('S','shared'),
    )
    bathrooms = models.IntegerField()
    bedrooms = models.IntegerField()
    beds = models.IntegerField()
    city = models.CharField(max_length=50)
    person_capacity = models.IntegerField()
    host_thumbnail_url=models.ImageField(upload_to='pictures/host/', null=True)
    host_thumbnail_url_small=models.ImageField(upload_to='pictures/host/', null=True)
    lat = models.FloatField()
    lng = models.FloatField()
    room_name = models.CharField(max_length=200)
    room_type = models.CharField(max_length=1, choices=ROOM_TYPES)
    price = models.IntegerField()
    amenities = models.ForeignKey('Amenity', on_delete=models.SET_NULL, null=True)
    house_img_urls = models.ForeignKey('HouseImgs', on_delete=models.SET_NULL, null=True)


class Amenity(models.Model):
    title = models.CharField(max_length=30)


class HouseImgs(models.Model):
    url = models.URLField()

