# Generated by Django 3.2.6 on 2021-08-12 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0003_auto_20210811_1941'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribedcity',
            name='notification',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
