# Generated by Django 3.2.6 on 2021-08-16 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0010_subscribedcity_last_run_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribedcity',
            name='last_run_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]