from django.urls import path
from django.urls import include
from rest_framework import routers

from .views import ContinentView
from .views import CountryView
from .views import CityView
from .views import FakeData

# Create your urls here.


router = routers.DefaultRouter()
router.register('continent', ContinentView)
router.register('country', CountryView)
router.register('city', CityView)

urlpatterns = [
    path('', include(router.urls)),
    path('fake/', FakeData.as_view(), name='fake_view'),
]