# Generated by Django 3.2.6 on 2021-08-13 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0005_weather'),
    ]

    operations = [
        migrations.AddField(
            model_name='weather',
            name='city_name',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
