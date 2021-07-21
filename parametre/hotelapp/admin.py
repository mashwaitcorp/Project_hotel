from django.contrib import admin
from .models.hotel import HotelCategory, Hotel
from .models.room_hotel import RoomCategory, RoomHotel

# Register your models here.

admin.site.register(HotelCategory)
admin.site.register(Hotel)

admin.site.register(RoomCategory)
admin.site.register(RoomHotel)
