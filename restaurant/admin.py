from django.contrib import admin
from .models import Menu, Booking  # Import the Menu and Booking models

# Register the Menu and Booking models with the admin site
admin.site.register(Menu)
admin.site.register(Booking)