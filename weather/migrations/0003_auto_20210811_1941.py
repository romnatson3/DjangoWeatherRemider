# Generated by Django 3.2.6 on 2021-08-11 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_auto_20210811_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='country',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='city',
            name='lat',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='lon',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='state',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
