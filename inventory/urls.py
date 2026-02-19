from django.urls import path
from .views import (
    VehicleListCreateView,
    VehicleDetailView,
    BookingListCreateView,
    BookingDetailView
)

urlpatterns = [

    path('vehicles/', VehicleListCreateView.as_view()),
    path('vehicles/<int:pk>/', VehicleDetailView.as_view()),

    path('bookings/', BookingListCreateView.as_view()),
    path('bookings/<int:pk>/', BookingDetailView.as_view()),
]
