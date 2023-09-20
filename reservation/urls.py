from django.conf.urls import url
from .views import AllHotels, AllCustomers, AllReservations
from .api import HotelAPI, CustomerAPI, AirportAPI
from rest_framework.routers import DefaultRouter
from django.urls import path, include

urlpatterns = [
    path('api/hotels/', HotelAPI.as_view()),
    path('api/customer/', CustomerAPI.as_view()),
    path('api/airport/', AirportAPI.as_view()),
    path('allhotels/', AllHotels),
    path('allcustomers/', AllCustomers),
    path('allreservations/', AllReservations)
    
]
