from django.test import TestCase
from weather.models import User, Weather, City, SubscribedCity


class TestModel(TestCase):
    def setUp(self):
        test = User.objects.create(username='test', first_name='test')
        city = City.objects.create(id=1, name='Lviv', state='', country='UA', lon=20.5, lat=20.5)
        subscribed_city = SubscribedCity.objects.create(user=test, city=city, notification=1)
        weather = Weather.objects.create(
            city_id = city,
            main = 'Clouds',
            city_name = 'Lviv',
            description = 'Clouds',
            temp = 20.1,
            temp_min = 20.1,
            temp_max = 20.1,
            pressure = 1000,
            humidity = 90,
            wind_speed = 12
        )

    def tearDown(self):
        pass

    def test_city_name_label(self):
        city = City.objects.first()
        field_label = city._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_weather_name_label(self):
        weather = Weather.objects.first()
        field_label = weather._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_object_id(self):
        subscribed_city = SubscribedCity.objects.get(id=1)
        city = City.objects.get(id=1)
        self.assertEquals(subscribed_city.city, city)
