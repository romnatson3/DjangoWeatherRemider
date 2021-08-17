from rest_framework import serializers
from weather.models import City, SubscribedCity, Weather


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model=City
        fields='__all__'


class SubscribedCitySerializer(serializers.ModelSerializer):
    class Meta:
        model=SubscribedCity
        fields='__all__'


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Weather
        fields='__all__'
