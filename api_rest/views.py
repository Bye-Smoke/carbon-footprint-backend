from rest_framework import status
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.viewsets import ModelViewSet

from footprint.models import Continent
from footprint.models import Country
from footprint.models import City
from .serializers import ContinentSerializer
from .serializers import CountrySerializer
from .serializers import CitySerializer
from .utils import generate_fake_data

# Create your views here.


class ContinentView(ModelViewSet):
    queryset = Continent.objects.all()
    serializer_class = ContinentSerializer


class CountryView(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CityView(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class FakeData(APIView):
    
    def post(self, request):
        json = JSONParser().parse(request)
        number = int(json.get('number'))
        if number:
            generate_fake_data(number)
            content = {'successful data generation': 'fake data'}
            return JsonResponse(content, status=status.HTTP_200_OK)
        
        content = {'please send number': 'nothing to see here'}
        return JsonResponse(content, status=status.HTTP_400_BAD_REQUEST)
