from django.urls import path
from .views import HotelCreate

urlpatterns = [
   
    path('', HotelCreate.as_view(), name="create"),
    
]