from django.urls import path
from .views import home_hotel

urlpatterns = [
    path('', home_hotel, name='home_hotel'),
    
]