from main.celery import app
from django.core.mail import send_mail
from main.settings import OPENWEATHERMAP_URL, QUERY_PARAMETERS
from weather.serializers import CitySerializer, SubscribedCitySerializer, WeatherSerializer
from weather.models import City, SubscribedCity, Weather
import requests
import json
from django.utils import timezone


def get_weather_by_id(city_id):
    QUERY_PARAMETERS['id'] = city_id
    response = requests.get(OPENWEATHERMAP_URL, params=QUERY_PARAMETERS)
    if response.status_code == 200:
        content = json.loads(response.content)
        weather = dict(
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
        )
        return weather


@app.task
def request_weather_server():
    cities = SubscribedCity.objects.all().values('city').distinct()
    for i in cities:
        weather = get_weather_by_id(i['city'])
        serializer = WeatherSerializer(data=weather)
        if serializer.is_valid():
            serializer.save()


@app.task
def subscribed_city_beat():
    subscribed_city = SubscribedCity.objects.all()
    for i in subscribed_city:
        td = timezone.now() - i.last_run_at
        hours = td.seconds // 3600
        if i.notification <= hours:
            w = Weather.objects.filter(city_id=i.city).last()
            last_weather_str = f'{w.description}\ntemp: {w.temp}\nhumidity: {w.humidity}\npressure: {w.pressure}\nwind_speed: {w.wind_speed}'
            send_mail_task.delay(i.user.email, i.city.name, last_weather_str)
            i.last_run_at = timezone.now()
            i.save()


@app.task(retry=False)
def send_mail_task(email, city_name, last_weather_str):
    send_mail(
        f'Weather notification for {city_name}',
        last_weather_str,
        'info@rns.pp.ua',
        [email],
        fail_silently=False
    )
