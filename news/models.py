from django.db import models
from datetime import datetime
# Create your models here.
from listings.models import Listing


class News(models.Model):
    Heading = models.CharField(max_length=50)
    Headlines = models.CharField(max_length=200)
    img_disp = models.ImageField(
        upload_to='photos/%Y/%m/%d/', height_field=None, width_field=None)
    img_main = models.ImageField(
        upload_to='photos/%Y/%m/%d/', height_field=None, width_field=None, blank=True)
    summary = models.TextField(max_length=200)
    status = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.Heading


class Review(models.Model):
    project = models.ForeignKey(Listing, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    review = models.TextField(blank=False, max_length=250)
    img_disp = models.ImageField(
        upload_to='photos/%Y/%m/%d/', height_field=None, width_field=None)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
