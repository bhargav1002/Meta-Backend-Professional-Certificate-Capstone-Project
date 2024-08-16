from django.shortcuts import render
from rest_framework import generics
from .models import Menu
from .serializers import MenuSerializer
from rest_framework import viewsets
from .models import Booking
from .serializers import BookingSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

# Handles POST and GET requests for the Menu items
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()  # Retrieves all Menu items from the database
    serializer_class = MenuSerializer  # Specifies the serializer to use for Menu items


# Handles GET, PUT, and DELETE requests for a single Menu item
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()  # Retrieves all Menu items from the database
    serializer_class = MenuSerializer  # Specifies the serializer to use for Menu items

# Handles CRUD operations for the Booking model
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
