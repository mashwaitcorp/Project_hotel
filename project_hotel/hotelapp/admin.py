from django.contrib import admin
# import model class hotel , room,reservation, booking, price_plan 
from .models.hotel import HotelCategory, Hotel
from .models.room_hotel import RoomCategory, RoomHotel
from .models.reservation import Reservation
from .models.booking import BookingRoom
from .models.price_plan import PricePlan
from .models.admin import Admin
from .models.customer import Customer

# Register your models here.

admin.site.register(HotelCategory)
admin.site.register(Hotel)

admin.site.register(RoomCategory)
admin.site.register(RoomHotel)

admin.site.register(Reservation)

admin.site.register(BookingRoom)

admin.site.register(PricePlan)

admin.site.register(Admin)

admin.site.register(Customer)
