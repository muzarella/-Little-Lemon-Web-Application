from django.db import models
from datetime import datetime
# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    no_of_guests = models.IntegerField(null=True, blank=True)
    booking_date = models.DateTimeField(default=datetime.now, null=True, blank=True)

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return f'{self.title} : {str(self.price)}'