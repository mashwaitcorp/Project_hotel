from django.urls import path
from .views import home_customer

urlpatterns = [
    path('', home_customer, name='home_customer'),
    
]
