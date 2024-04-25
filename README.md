# Reservations

This Backend Django project is designed to manage hotel reservations along with customer information and flight details.

## Features:

- **Hotel Management:** Allows adding, updating, and deleting hotels with their respective details such as name, city, total rooms, empty rooms, and price.
- **Customer Management:** Provides functionality to manage customer information including name, phone number, and email.
- **Airport Management:** Enables adding airports with their company information.
- **Flight Management:** Allows adding flight details including origin and destination.
- **Reservation System:** Facilitates making reservations for hotels, associating customers, airports, and flights, along with start and end times.

## Project Structure:

- **Models:**
  - `Hotel`: Represents hotel information such as name, city, total rooms, empty rooms, and price.
  - `Customer`: Stores customer details like name, phone number, and email.
  - `Airport`: Manages airport information including name and company.
  - `Flight`: Contains flight details like origin and destination.
  - `Reservation`: Handles reservations linking hotels, customers, airports, flights, and reservation times.

- **Serializers:**
  - `HotelSerializer`: Serializes hotel objects for API responses.
  - `CustomerSerializer`: Serializes customer objects for API responses.
  - `AirportSerializer`: Serializes airport objects for API responses.

- **Views:**
  - `AllHotels`: Renders a view displaying all hotels.
  - `AllCustomers`: Renders a view displaying all customers.
  - `AllReservations`: Renders a view displaying all reservations.

## How to Run:

1. Make sure you have Python and Django installed on your system.
2. Clone this repository to your local machine: git clone 
3. Navigate to the project directory.
4. Run `python manage.py migrate` to apply migrations.
5. Start the Django development server by running `python manage.py runserver`.
6. Access the application through the provided URLs.


- Django: [link to Django](https://www.djangoproject.com/)
- Django REST Framework: [link to DRF](https://www.django-rest-framework.org/)



