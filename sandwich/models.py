from django.db import models
from django.conf import settings
import os
import uuid

# Create your models here.

class Retailer(models.Model):
    """
    Lots of money sapping pricks.
    """
    name = models.CharField(max_length=50)


class Sandwich(models.Model):
    """
    A table for all the glorious Christmas sandwiches the world has provided us.
    """
    name = models.CharField(max_length=200)
    barcode = models.CharField(max_length=30, blank=True)
    image = models.ImageField(upload_to=os.path.join(settings.MEDIA_ROOT, "images", str(uuid.uuid4())))
