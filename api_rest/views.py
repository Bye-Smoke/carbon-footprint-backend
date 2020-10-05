from rest_framework.viewsets import ModelViewSet

from footprint.models import Continent
from footprint.models import Country
from footprint.models import City
from .serializers import ContinentSerializer
from .serializers import CountrySerializer
from .serializers import CitySerializer

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
