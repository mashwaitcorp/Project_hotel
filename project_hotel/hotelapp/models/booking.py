from django.db import models


class BookingRoom(models.Model):
    
    booking_time = models.DateTimeField(auto_now=True, verbose_name="Date_heure du pan de servation")
    start_date = models.DateTimeField(auto_now=True, verbose_name="Date d'arrivée")
    end_date = models.DateTimeField(auto_now=True, verbose_name="Date de sortie")
    #client = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    #room = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    child_count = models.IntegerField(null=False, blank=True, verbose_name="Nombre des personnes")
    discount_coupe = models.IntegerField(null=False, blank=True, verbose_name="Montant de reduction")
    total_cost = models.IntegerField(null=False, blank=True, verbose_name="Total prix")
    payement_amount = models.IntegerField(null=False, blank=True, verbose_name="Montant à payer")
    payement_type = models.IntegerField(null=False, blank=True, verbose_name="Type de payement")
    is_block = models.IntegerField(null=False, blank=True, verbose_name="plan de reservation bloqué")
    is_delete = models.IntegerField(null=False, blank=True, verbose_name="plan de reservation supprimé")
    
    class Meta:
            ordering = ['-start_date']
            verbose_name = ('Plan reservation')
            verbose_name_plural = ('Plans de reservations')

    # def __unicode__(self):
    #     return u'%s' % self.client