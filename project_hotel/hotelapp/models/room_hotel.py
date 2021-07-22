from django.db import models

# Create your models here.

class RoomCategory(models.Model):
    room_category_name = models.CharField(max_length=255, null=False, blank=True, verbose_name="Nom categorie")
    hotel_decription = models.TextField(verbose_name="Description chambre")

    class Meta:
        verbose_name = "Categorie chambre"
        verbose_name_plural = "Categories chambres"
        ordering = ['room_category_name']

    def __str__(self):
        return self.room_category_name
    

class RoomHotel(models.Model):
    room_name = models.CharField(max_length=255, null=False, blank=True, verbose_name="Nom chambre")
    room_number = models.IntegerField(null=False, blank=True, verbose_name="Numero chambre")
    room_capacity = models.IntegerField(null=False, blank=True, verbose_name="Capacité")
    hotel_type = models.ForeignKey(RoomCategory, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Categorie chambre")
    room_image = models.ImageField(upload_to='room_image/', null=False, blank=True)



    class Meta:
        verbose_name = "Chambre hotel"
        verbose_name_plural = "Chambres hotels"
        ordering = ['room_name']

    def __str__(self):
        return self.room_name
