from rest_framework.test import APITestCase, APIClient
from weather.models import User, Weather, City, SubscribedCity
from django.urls import reverse



class TestView(APITestCase):

    city_url = reverse('city', args=['lviv'])
    subscribe_url = reverse('subscribe')
    weather_url = reverse('weather')

    def setUp(self):
        city = City.objects.create(id=702550, name='Lviv', state='', country='UA', lon=20.5, lat=20.5)
        self.client = APIClient()
        response = self.client.post('/auth/users/', data={'username':'test','password':'Qw451223'})
        response = self.client.post('/auth/jwt/create/', data={'username':'test','password':'Qw451223'})
        token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION = 'Bearer ' + token)


    def tearDown(self):
        pass


    def test_create_user(self):
        response = self.client.get('/auth/users/me/')
        self.assertEqual(response.status_code, 200)


    def test_get_city(self):
        response = self.client.get(self.city_url)
        self.assertEqual(response.status_code, 200)


    def test_subscribed_city(self):
        response = self.client.post(self.subscribe_url, data={'user':1, 'city':702550, 'notification':1})
        self.assertEqual(response.status_code, 201)


    def test_get_weather(self):
        self.client.post(self.subscribe_url, data={'user':1, 'city':702550, 'notification':1})
        response = self.client.get(self.weather_url)
        self.assertEqual(response.status_code, 200)



