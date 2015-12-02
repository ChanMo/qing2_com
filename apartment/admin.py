from django.contrib import admin
from .models import Apartment

class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'longitude', 'latitude', 'is_real')

admin.site.register(Apartment, ApartmentAdmin)
