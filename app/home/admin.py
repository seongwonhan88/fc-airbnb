from django.contrib import admin

# Register your models here.
from .models import Amenity, Room, RoomInfo, HostImages, Booking

admin.site.register(Room)
admin.site.register(Amenity)
admin.site.register(RoomInfo)
admin.site.register(HostImages)
admin.site.register(Booking)
