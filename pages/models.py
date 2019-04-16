from django.db import models
from django import forms
#from phonenumber_field.modelfields import PhoneNumberField


class Carousel(models.Model):
    name = models.CharField(max_length=50, blank=True)
    display_Image = models.ImageField(
        upload_to='photos/%Y/%m/%d/', height_field=None, width_field=None)

    def __str__(self):
        return self.name


class Employee(models.Model):
    First_name = models.CharField(max_length=50, blank=False, default="")
    Last_name = models.CharField(max_length=30, blank=False, default="")
    display_Image = models.ImageField(
        upload_to='photos/%Y/%m/%d/', height_field=None, width_field=None)
    designation = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    phone = models.CharField(max_length=10, null=False,
                             blank=False, unique=True)

    def __str__(self):
        return self.First_name


class About(models.Model):
    name = models.CharField(max_length=50, blank=True)
    display_img = models.ImageField(
        upload_to='photos/%Y/%m/%d/', height_field=None, width_field=None, null=True)
    ceo_img = models.ImageField(
        upload_to='photos/%Y/%m/%d/', height_field=None, width_field=None, null=True)

    def __str__(self):
        return self.name
