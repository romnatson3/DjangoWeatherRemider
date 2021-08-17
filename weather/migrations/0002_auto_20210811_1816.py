# Generated by Django 3.2.6 on 2021-08-11 18:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribedcity',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='weather.city'),
        ),
        migrations.AlterUniqueTogether(
            name='subscribedcity',
            unique_together={('user', 'city')},
        ),
    ]