
from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import HotelSerializer , CustomerSerializer , AirportSerializer
from .models import Hotel, Customer, Airport
import django_filters.rest_framework

class HotelAPI(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['hotel_city', 'total_rooms', 'empty_rooms']

class CustomerAPI (generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name', 'email']
class AirportAPI (generics.ListCreateAPIView):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer
   