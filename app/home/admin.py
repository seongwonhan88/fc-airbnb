from django.contrib import admin

# Register your models here.
from .models import Amenity, HouseImgs, Room

admin.site.register(Room)
admin.site.register(HouseImgs)
admin.site.register(Amenity)