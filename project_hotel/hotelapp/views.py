from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models.hotel import Hotel
from .forms.form import HotelForm

# Create your views here.


class HotelCreate(CreateView):
    """
    Affichage du formulaire
    """
    model = Hotel
    form_class = HotelForm
    template_name="templates_hotel/index.html"
    