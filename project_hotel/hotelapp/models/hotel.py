from django.db import models

# Create your models here.

class HotelCategory(models.Model):
    hotel_category_name = models.CharField(max_length=255, null=False, blank=True, verbose_name="Nom categorie")
    hotel_decription = models.TextField(null=False, verbose_name="Description")


    class Meta:
        verbose_name = "Categorie hotel"
        verbose_name_plural = "Categories hotels"
        ordering = ['hotel_category_name']

    def __str__(self):
        return self.hotel_category_name

class Hotel(models.Model):
    hotel_name = models.CharField(max_length=255, null=False, blank=True, verbose_name="Nom")
    hotel_categry = models.ForeignKey(HotelCategory, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Categorie")
    hotel_address = models.CharField(max_length=255, null=False, blank=True, verbose_name="Addresse")
    hotel_image = models.ImageField(upload_to='hotel_image/', null=False, blank=True)


    class Meta:
        verbose_name = "Hotel"
        verbose_name_plural = "Hotels"
        ordering = ['hotel_name']

    def __str__(self):
        return self.hotel_name