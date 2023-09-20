# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django_prices.models import MoneyField, TaxedMoneyField
# Create your models here.

class Hotel(models.Model):
    hotel_name = models.CharField(max_length=100)
    hotel_city = models.CharField(max_length=100)
    total_rooms = models.IntegerField()
    empty_rooms = models.IntegerField()
    price_net_amount = models.DecimalField(max_digits=9, decimal_places=2, default="5")
    def __str__(self):
        return self.hotel_name

class Customer(models.Model):
    name = models.CharField(max_length=100)
    
    phone_num = models.CharField(max_length=20)
    
    email = models.EmailField(max_length=100, default='')

    
    
    def __str__(self):
        return self.name

class Airport(models.Model): 
    
    airport = models.CharField(max_length=100, default='') 
    company = models.CharField(max_length=100) 
    
     
    def __str__(self):
        return self.airport 

class Flight(models.Model): 
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    
    def __str__(self):
        return self.origin 

class Reservation(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    name = models.ForeignKey(Customer, on_delete=models.CASCADE)
    airport = models.ForeignKey(Airport, null=True, on_delete=models.CASCADE)
    destination = models.ForeignKey(Flight, null=True, on_delete=models.CASCADE)
    
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.hotel.hotel_name + " for " + self.name.name

 
 