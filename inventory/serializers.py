from rest_framework import serializers
from django.utils import timezone
from .models import Vehicle, Booking

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ['total_amount']

    def validate(self, data):

        vehicle = data.get('vehicle')
        start_date = data.get('start_date')
        end_date = data.get('end_date')

        if start_date < timezone.now().date():
            raise serializers.ValidationError("Start date cannot be in past")

        if end_date <= start_date:
            raise serializers.ValidationError("End date must be after start date")

        old_bookings = Booking.objects.filter(vehicle=vehicle)

        for booking in old_bookings:
            if start_date < booking.end_date and end_date > booking.start_date:
                raise serializers.ValidationError("Vehicle already booked for these dates")

        return data
