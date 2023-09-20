# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-09 09:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_num', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=100)),
                ('hotel_city', models.CharField(max_length=100)),
                ('total_rooms', models.IntegerField()),
                ('empty_rooms', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservation.Customer')),
                ('Hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservation.Hotel')),
            ],
        ),
    ]
