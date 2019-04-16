from django.db import models
from datetime import datetime
# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=13,null=True)
    locality = models.CharField(max_length=50,null=True)
    subject = models.CharField(max_length=100,null=True)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.name

class Contact_Specific(models.Model):
    name = models.CharField(max_length=200)
    prop =  models.CharField(max_length=200)
    prop_Id =  models.CharField(max_length=20)
    prop_address=models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=13,null=True)
    locality = models.CharField(max_length=50,null=True)
    subject = models.CharField(max_length=100,null=True)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.name
