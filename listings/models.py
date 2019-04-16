from django.db import models
from datetime import datetime
# Create your models here.
status_ch = (
    ('Available', 'Available'),
    ('Sold', 'Sold'),
    ('On-Hold', 'On-Hold'),
)

categories_ch = (
    ('Ongoing', 'Ongoing'),
    ('Buy', 'Buy'),
    ('Rent', 'Rent'),

)


class Listing(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=20, choices=categories_ch)
    address = models.CharField(max_length=200)
    img_disp = models.ImageField(
        upload_to='photos/%Y/%m/%d/', height_field=None, width_field=None,  null=True)
    img_1 = models.ImageField(
        upload_to='photos/%Y/%m/%d/', height_field=None, width_field=None)
    img_2 = models.ImageField(
        upload_to='photos/%Y/%m/%d/', height_field=None, width_field=None)
    img_3 = models.ImageField(
        upload_to='photos/%Y/%m/%d/', height_field=None, width_field=None)
    img_4 = models.ImageField(
        upload_to='photos/%Y/%m/%d/', height_field=None, width_field=None, blank=True)
    floor_plan1 = models.ImageField(
        upload_to='photos/%Y/%m/%d/', height_field=None, width_field=None, blank=True, null=True)
    floor_plan2 = models.ImageField(
        upload_to='photos/%Y/%m/%d/', height_field=None, width_field=None, blank=True, null=True)
    floor_plan3 = models.ImageField(
        upload_to='photos/%Y/%m/%d/', height_field=None, width_field=None, blank=True, null=True)
    floor_plan4 = models.ImageField(
        upload_to='photos/%Y/%m/%d/', height_field=None, width_field=None, blank=True, null=True)
    desc = models.TextField(max_length=200)
    prop_Id = models.IntegerField(blank=True)
    location = models.CharField(max_length=200)
    prop_type = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=status_ch)
    area = models.IntegerField(blank=False)
    Bedrooms = models.IntegerField(blank=False)
    Bath = models.IntegerField(blank=False)
    parking = models.CharField(max_length=40)
    amen1 = models.CharField(max_length=40, blank=True)
    amen2 = models.CharField(max_length=40, blank=True)
    amen3 = models.CharField(max_length=40, blank=True)
    amen4 = models.CharField(max_length=40, blank=True)
    amen5 = models.CharField(max_length=40, blank=True)
    amen6 = models.CharField(max_length=40, blank=True)
    map_link = models.CharField(max_length=350, blank=True)
    video_link = models.CharField(max_length=250, blank=True)
    is_published = models.BooleanField(default=True)
    sold = models.BooleanField(default=False)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
