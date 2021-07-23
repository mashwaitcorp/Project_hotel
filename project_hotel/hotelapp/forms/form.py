from django import forms
from django.db import models
from ..models.hotel import HotelCategory, Hotel
from ..models.room_hotel import RoomCategory, RoomHotel
from ..models.booking import BookingRoom
from ..models.reservation import Reservation
from ..models.price_plan import PricePlan




class HotelCategoryForm(forms.ModelForm):
    class Meta:
        model = HotelCategory
        fields = ('hotel_category_name','hotel_decription')

        widgets = {
            'hotel_category_name': forms.TextInput(attrs={'class': 'form-control'}),
            'hotel_decription': forms.TextInput(attrs={'class': 'form-control'}),
        }

class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ('hotel_name','hotel_categry','hotel_address','hotel_image')

        widgets = {
            'hotel_name': forms.TextInput(attrs={'class': 'form-control'}),
            'hotel_categry': forms.Select(attrs={'class': 'form-control'}),
            'hotel_address': forms.TextInput(attrs={'class': 'form-control'}),
            'hotel_image': forms.FileInput(attrs={'class': 'form-control'}),
        }

class RoomCategoryForm(forms.ModelForm):
    class Meta:
        model = RoomCategory
        fields = ('room_category_name','hotel_decription')

        widgets = {
            'room_category_name': forms.TextInput(attrs={'class': 'form-control'}),
            'hotel_decription': forms.TextInput(attrs={'class': 'form-control'}),
        }


class HotelForm(forms.ModelForm):
    class Meta:
        model = RoomHotel
        fields = ('room_name','room_number','room_capacity','hotel_type','room_image')

        widgets = {
            'room_name': forms.TextInput(attrs={'class': 'form-control'}),
            'hotel_type': forms.Select(attrs={'class': 'form-control'}),
            'room_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'room_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'room_image': forms.FileInput(attrs={'class': 'form-control'}),
        }


class PricePlanForm(forms.ModelForm):
    class Meta:
        
        model = PricePlan
        fields = ('room_type','sun_d','tue_d','Wed_d','Wed_d','thu_d','fri_d',
                  'sat_d','description')

        widgets = {
            'room_type': forms.Select(attrs={'class': 'form-control'}),
            #'start_date': forms.DateInput(attrs={'class': 'form-control'}),
            #'end_date': forms.TextInput(attrs={'class': 'form-control'}),
            'sun_d': forms.TextInput(attrs={'class': 'form-control'}),
            'tue_d': forms.TextInput(attrs={'class': 'form-control'}),
            'Wed_d': forms.TextInput(attrs={'class': 'form-control'}),
            'thu_d': forms.TextInput(attrs={'class': 'form-control'}),
            'fri_d': forms.TextInput(attrs={'class': 'form-control'}),
            'sat_d': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            
        }