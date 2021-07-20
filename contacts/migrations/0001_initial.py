# Generated by Django 3.2.4 on 2021-07-20 04:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('car_id', models.IntegerField()),
                ('customer_need', models.CharField(max_length=255)),
                ('car_title', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('message', models.TextField(blank=True)),
                ('user_id', models.IntegerField(blank=True)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
