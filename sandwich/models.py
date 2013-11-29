from django.db import models
from django.conf import settings
import os
import uuid

# Create your models here.

class ModelUtils(object):
    """
    A big fucking sack of static helper methods
    """

    @staticmethod
    def get_image_path(instance, filename):
        """
        Returns a filepath for the tasty image to be uploaded to
        """
        name, ext = os.path.splitext(filename)
        filename = "{0}.{1}".format(uuid.uuid4(), ext)
        return os.path.join(settings.MEDIA_ROOT, 'images', filename)

class Retailer(models.Model):
    """
    Lots of money sapping pricks.
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Sandwich(models.Model):
    """
    A table for all the glorious Christmas sandwiches the world has provided us.
    """
    name = models.CharField(max_length=200)
    barcode = models.CharField(max_length=30, blank=True)
    image = models.ImageField(upload_to=ModelUtils.get_image_path)
    retailer = models.ForeignKey(Retailer)

    def __str__(self):
        return "{0}: {1}".format(self.retailer.name, self.name)


class Rating(models.Model):
    """
    A fokin' individual rating on a bloody festive sandwich.
    """
    RATING_CHOICES = [(i, i) for i in range(1, 6)]

    rating = models.IntegerField(choices=RATING_CHOICES)
    sandwich = models.ForeignKey(Sandwich)

    def __str__(self):
        return '{0}: {1}'.format(self.sandwich.name[:15], self.rating)

class Tag(models.Model):
    """
    Tags for saying what a sandwich has in it, e.g. this sandwich has a fuckton
    of turkey.
    """
    name = models.CharField(max_length=20)
    sandwich = models.ForeignKey(Sandwich)

    def __str__(self):
        return self.name
