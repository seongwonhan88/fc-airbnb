from django.contrib import admin

# Register your models here.
from .models import Amenity, Room, HostImages, Booking, Review

admin.site.register(Room)
admin.site.register(Amenity)
admin.site.register(HostImages)
admin.site.register(Booking)
admin.site.register(Review)
