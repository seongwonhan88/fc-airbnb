from django.db.models import Avg
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Room


class CityAveragePriceAPIView(APIView):
    CITIES = (
        '서울', '부산', '제주'
    )

    def get(self, request):
        average = dict()

        for city in self.CITIES:
            room = Room.objects.filter(public_address__contains=city).aggregate(Avg('price'))
            price_avg = room['price__avg']
            average[f'{city}_average'] = int(price_avg)

        return Response(average)