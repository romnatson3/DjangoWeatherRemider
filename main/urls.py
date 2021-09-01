"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import routers
from weather.views import CityView, SubscribedCityView, SubscribedCityViewEdit, WeatherView
from django.views.static import serve
from .settings import STATIC_ROOT


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('api/city/(?P<name>\w+)/$', CityView.as_view(), name='city'),
    path('api/subscribe/', SubscribedCityView.as_view(), name='subscribe'),
    re_path('api/subscribe/(?P<id>[0-9]+)/$', SubscribedCityViewEdit.as_view(), name='subscribe_edit'),
    path('api/weather/', WeatherView.as_view(), name='weather'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    re_path(r'static/(?P<path>.*)$', serve, {'document_root':STATIC_ROOT}),
]
