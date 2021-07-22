from django.db import models
# import the model class room, booking
from ..models.room_hotel import RoomHotel
from ..models.booking import BookingRoom

# Create your models here.


class Reservation(models.Model):
    booking_id = models.ForeignKey(BookingRoom, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Chambre")
    room_name = models.ForeignKey(RoomHotel, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Chambre")
    description = models.TextField(null=False)

    class Meta:
        verbose_name = "Reservation"
        verbose_name_plural = "Reservations"
        ordering = ['room_name']

    def __str__(self):
        return self.room_name