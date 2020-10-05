from rest_framework import routers, serializers, viewsets

from footprint.models import Continent
from footprint.models import Country
from footprint.models import City

# Create your serializers here.


class ContinentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Continent
        fields = '__all__'


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = '__all__'
