import django_filters

from .models import Room


class RoomFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Room
        fields = {
            'id': ['exact'],
            'city': ['contains'],
            'bathrooms': ['lte', 'gte', 'exact'],
            'bedrooms': ['lte', 'gte', 'exact'],
            'beds': ['lte', 'gte', 'exact'],
            'person_capacity': ['lte', 'gte', 'exact'],
            'room_name': ['contains'],
            'room_type': ['exact'],
            'room_and_property_type': ['contains'],
            'public_address': ['contains', 'exact'],
            'price': ['lte', 'gte', 'exact'],
            'amenities__help_text': ['contains'],
        }
