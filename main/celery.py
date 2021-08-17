import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
app = Celery('main')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'request-weather-server-every-hour': {
        'task': 'weather.tasks.request_weather_server',
        'schedule': crontab(minute=0, hour='*/1'),
        'args': (),
    },
    'scan-subscribed-city': {
        'task': 'weather.tasks.subscribed_city_beat',
        'schedule': crontab(minute='*/30'),
        'args': (),
    },
}
