from django.contrib import admin

# Register your models here.
from sandwich.models import Sandwich, Retailer, Rating

admin.site.register(Sandwich)
admin.site.register(Retailer)
admin.site.register(Rating)
