from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class City(models.Model):

    class Meta():
        verbose_name = 'city'
        indexes = [
           models.Index(fields=['name']),
        ]

    id = models.IntegerField(primary_key=True, blank=False)
    name = models.CharField(max_length=256, blank=False)
    state = models.CharField(max_length=256, blank=True)
    country = models.CharField(max_length=256, blank=True)
    lon = models.FloatField(blank=True)
    lat = models.FloatField(blank=True)



class SubscribedCity(models.Model):

    class Meta():
        verbose_name = 'subscribed_city'
        unique_together = ('user', 'city')

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    notification = models.IntegerField(blank=False)
    last_run_at = models.DateTimeField(auto_now_add=True)


class Weather(models.Model):

    class Meta():
        verbose_name = 'weather'

    city_id = models.ForeignKey(City, on_delete=models.PROTECT, db_column='city_id')
    datetime = models.DateTimeField(auto_now_add=True)
    main = models.CharField(max_length=256, blank=True)
    city_name = models.CharField(max_length=256, blank=True)
    description = models.CharField(max_length=256, blank=True)
    temp = models.FloatField(blank=True)
    temp_min = models.FloatField(blank=True)
    temp_max = models.FloatField(blank=True)
    pressure = models.FloatField(blank=True)
    humidity = models.FloatField(blank=True)
    wind_speed = models.FloatField(blank=True)

