# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Hotel, Customer, Reservation

def AllHotels(request):
    return render(request, "reservation/hotels.html", {'hotels': Hotel.objects.all()})

def AllCustomers(request):
    return render(request, "reservation/customers.html", {'customers': Customer.objects.all()})


def AllReservations(request):
    return render(request, "reservation/reservations.html", {'reservations': Reservation.objects.all()})

