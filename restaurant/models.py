from django.db import models

class Menu(models.Model):
    title = models.CharField(max_length=255)  # Title field with a max length of 255 characters
    price = models.DecimalField(max_digits=6, decimal_places=2)  # Price field with max digits 10 and 2 decimal places
    inventory = models.SmallIntegerField()  # Inventory field as an integer

    def get_item(self):
        return f'{self.title} : {str(self.price)}'


class Booking(models.Model):
    name = models.CharField(max_length=255)  # Name field with a max length of 255 characters
    no_of_guests = models.IntegerField()  # Number of guests field as an integer
    booking_date = models.DateTimeField()  # Booking date field as a datetime

    def __str__(self):
        return f"Booking for {self.name} on {self.booking_date}"