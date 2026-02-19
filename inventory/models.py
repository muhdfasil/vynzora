from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
class Vehicle(models.Model):

    FUEL_CHOICES = [
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Electric', 'Electric'),
        ('Hybrid', 'Hybrid'),
    ]

    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    year = models.IntegerField()
    price_per_day = models.DecimalField(max_digits=6, decimal_places=2)
    fuel_type = models.CharField(max_length=10, choices=FUEL_CHOICES)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Booking(models.Model):

    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    phone_validator = RegexValidator(regex=r'^\d{10}$',message='Phone number must be 10 digits')    
    customer_phone = models.CharField(max_length=10,validators=[phone_validator])

    start_date = models.DateField()
    end_date = models.DateField()

    total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        days = (self.end_date - self.start_date).days
        self.total_amount = days * self.vehicle.price_per_day
    
        super().save(*args, **kwargs)

        self.vehicle.is_available = False
        self.vehicle.save()

    def __str__(self):
        return self.customer_name
