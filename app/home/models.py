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
    host_thumbnail_url=models.ImageField(upload_to='pictures/host/', blank=True, null=True)
    host_thumbnail_url_small=models.ImageField(upload_to='pictures/host/', blank=True, null=True)
    lat = models.FloatField()
    lng = models.FloatField()
    room_name = models.CharField(max_length=200)
    room_type = models.CharField(max_length=1, choices=ROOM_TYPES)
    price = models.IntegerField()
    amenities = models.ForeignKey('Amenity', on_delete=models.SET_NULL, null=True, related_query_name='room_amenities')

    def __str__(self):
        return self.room_name

class Amenity(models.Model):
    room = models.ForeignKey('Room',
                             on_delete=models.SET_NULL,
                             null=True,
                             )
    title = models.CharField(max_length=30)


    def __str__(self):
        return self.title


class HouseImgs(models.Model):
    room = models.ForeignKey('Room',
                             on_delete=models.CASCADE,
                             related_name='room_house_imgs',)
    url = models.URLField()

    def __str__(self):
        return self.room