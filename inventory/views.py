from rest_framework import generics
from .models import Vehicle, Booking
from .serializers import VehicleSerializer, BookingSerializer


class VehicleListCreateView(generics.ListCreateAPIView):

    serializer_class = VehicleSerializer

    def get_queryset(self):
        queryset = Vehicle.objects.all()

        brand = self.request.query_params.get('brand')
        fuel_type = self.request.query_params.get('fuel_type')
        is_available = self.request.query_params.get('is_available')

        if brand:
            queryset = queryset.filter(brand=brand)

        if fuel_type:
            queryset = queryset.filter(fuel_type=fuel_type)

        if is_available:
            if is_available.lower() == 'true':
                queryset = queryset.filter(is_available=True)
            elif is_available.lower() == 'false':
                queryset = queryset.filter(is_available=False)

        return queryset


class VehicleDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class BookingListCreateView(generics.ListCreateAPIView):

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class BookingDetailView(generics.RetrieveAPIView):

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
