from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth.models import User
import random


class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        if Listing.objects.exists():
            self.stdout.write(self.style.WARNING("Listings already exist. Skipping seeding."))
            return

        sample_listings = [
            {"title": "Beachfront Villa", "description": "A beautiful villa by the sea", "price_per_night": 250.00, "location": "Mombasa"},
            {"title": "Mountain Cabin", "description": "Cozy cabin with mountain views", "price_per_night": 150.00, "location": "Mt. Kenya"},
            {"title": "City Apartment", "description": "Modern apartment in the city center", "price_per_night": 100.00, "location": "Nairobi"},
        ]

        for listing_data in sample_listings:
            listing = Listing.objects.create(**listing_data)
            self.stdout.write(self.style.SUCCESS(f"Created listing: {listing.title}"))

        # Optional: create dummy users
        for i in range(3):
            User.objects.create_user(username=f"user{i}", password="password123")

        self.stdout.write(self.style.SUCCESS("Database seeding completed successfully!"))
