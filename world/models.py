from django.contrib.gis.db import models
from django.utils import timezone
from users.models import Profile
from django.contrib.auth.models import User
from django.urls import reverse


class WorldBorder(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField('Population 2005')
    fips = models.CharField('FIPS Code', max_length=2, null=True)
    iso2 = models.CharField('2 Digit ISO', max_length=2)
    iso3 = models.CharField('3 Digit ISO', max_length=3)
    un = models.IntegerField('United Nations Code')
    region = models.IntegerField('Region Code')
    subregion = models.IntegerField('Sub-Region Code')
    lon = models.FloatField()
    lat = models.FloatField()

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    mpoly = models.MultiPolygonField()

    # Returns the string representation of the model.
    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    dream_holiday = models.OneToOneField(WorldBorder, on_delete=models.CASCADE, null=True)
    reason = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Flight(models.Model):
    airport_location = models.CharField('Origin Place', max_length=50)
    airport_code = models.CharField('Origin Airport Code', max_length=10)
    airport_lat = models.FloatField()
    airport_lon = models.FloatField()

    def __str__(self):
        return self.airport_location

