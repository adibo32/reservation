from rest_framework import serializers
from .models import Hotel, Customer, Airport

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        exclude = []

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        exclude = []

class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        exclude = []