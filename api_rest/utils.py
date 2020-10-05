from time import time
import random
from mixer.backend.django import mixer

from footprint.models import Continent
from footprint.models import Country
from footprint.models import City


def generate_fake_data(number):
    models = [Continent]

    for model in models:
        mixer.cycle(number).blend(model)
