from django.contrib import admin

# Register your models here.
from .models import Amenity, Room, HouseInfo

admin.site.register(Room)
admin.site.register(Amenity)
admin.site.register(HouseInfo)