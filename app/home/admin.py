from django.contrib import admin

# Register your models here.
from .models import Amenity, HouseImg, Room

admin.site.register(Room)
admin.site.register(HouseImg)
admin.site.register(Amenity)