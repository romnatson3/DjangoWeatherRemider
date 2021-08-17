from rest_framework import viewsets
from weather.models import City, SubscribedCity, Weather
from weather.serializers import CitySerializer, SubscribedCitySerializer, WeatherSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from main.settings import WEATHER_KEY, OPENWEATHERMAP_URL, QUERY_PARAMETERS
import requests
import json

# Create your views here.


class WeatherView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        subscribed_city = get_list_or_404(SubscribedCity, user=request.user)
        weather_list = []
        for i in subscribed_city:
            QUERY_PARAMETERS['id'] = i.city.id
            response = requests.get(OPENWEATHERMAP_URL, params=QUERY_PARAMETERS)
            if not response.status_code == 200:
                return Response(status=status.HTTP_404_NOT_FOUND)
            else:
                content = json.loads(response.content)
                weather_list.append(dict(
                    city_id=content['id'],
                    city_name=content['name'],
                    main = content['weather'][0]['main'],
                    description = content['weather'][0]['description'],
                    temp = content['main']['temp'],
                    temp_min = content['main']['temp_min'],
                    temp_max = content['main']['temp_max'],
                    pressure = content['main']['pressure'],
                    humidity = content['main']['humidity'],
                    wind_speed = content['wind']['speed']
                ))
        serializer = WeatherSerializer(data=weather_list, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)



class CityView(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, name):
        return get_list_or_404(City, name__icontains=name)

    def get(self, request, name, format=None):
        city = self.get_object(name)
        serializer = CitySerializer(city, many=True)
        return Response(serializer.data)



class SubscribedCityView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        subscribed_city = SubscribedCity.objects.filter(user=request.user).values('id', 'user_id', 'user__username', 'city_id', 'city__name', 'notification')
        return Response(subscribed_city)

    def post(self, request, format=None):
        serializer = SubscribedCitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class SubscribedCityViewEdit(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, id):
        return get_object_or_404(SubscribedCity, id=id)

    def get(self, request, id, format=None):
        subscribed_city = self.get_object(id)
        serializer = SubscribedCitySerializer(subscribed_city)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        subscribed_city = self.get_object(id)
        serializer = SubscribedCitySerializer(subscribed_city, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        subscribed_city = self.get_object(id)
        subscribed_city.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
