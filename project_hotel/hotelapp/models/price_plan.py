from django.db import models
# import the model class room
from ..models.room_hotel import RoomCategory

# Create your models here.


class PricePlan(models.Model):
    room_type = models.ForeignKey(RoomCategory, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Chambre")
    start_date = models.DateTimeField(auto_now=True, verbose_name="Date debut")
    end_date = models.DateTimeField(auto_now=True, verbose_name="Date de fin")
    sun = models.CharField(max_length=50,null=False, blank=True, verbose_name="Dimanche")
    mon = models.CharField(max_length=50,null=False, blank=True, verbose_name="Lundi")
    tue = models.CharField(max_length=50,null=False, blank=True, verbose_name="Mardi")
    Wed = models.CharField(max_length=50,null=False, blank=True, verbose_name="Mercredi")
    thu = models.CharField(max_length=50,null=False, blank=True, verbose_name="Jeudi")
    fri = models.CharField(max_length=50,null=False, blank=True, verbose_name="Vendredi")
    sat = models.CharField(max_length=50,null=False, blank=True, verbose_name="Samedi")
    description = models.TextField(null=False)

    class Meta:
        verbose_name = "Plan de prix"
        verbose_name_plural = "Plans de prix"
        ordering = ['room_type']

    def __str__(self):
        return self.room_type