from django.db import models

class Apartment(models.Model):
    name = models.CharField(max_length=200)
    longitude = models.DecimalField(max_digits=14, decimal_places=10)
    latitude = models.DecimalField(max_digits=13, decimal_places=10)
    is_real = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

