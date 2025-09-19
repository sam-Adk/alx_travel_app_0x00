# alx_travel_app_0x00

This project is a travel booking app built with Django and Django REST Framework.  
It includes models for Listings, Bookings, and Reviews, along with a database seeder.

## Features
- Listings with title, description, location, price per night
- Bookings linked to users and listings
- Reviews with rating and comment
- Database seeding with sample data

## Setup
```bash
git clone <repo-url>
cd alx_travel_app_0x00
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py seed
python manage.py runserver
