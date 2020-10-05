from django.db import models

# Create your models here.

class Footprint(models.Model):
    name = models.CharField(max_length=45)
    temperature = models.FloatField()
    mtco2 = models.FloatField()
    STATUS_CHOICES = [
        ('Good', 'good'),
        ('Medium', 'medium'),
        ('Danger', 'danger')
    ]
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES
    )

    class Meta:
        abstract = True


class Continent(Footprint):
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Country(Footprint):
    updated = models.DateTimeField(auto_now=True)

    continent = models.ForeignKey('Continent', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class City(Footprint):
    updated = models.DateTimeField(auto_now=True)

    country = models.ForeignKey('Country', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


# fecha de los datos
# descarga de los datos automaticamente (cada día)