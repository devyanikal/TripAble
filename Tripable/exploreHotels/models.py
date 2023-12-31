from django.db import models
from django.core.exceptions import FieldDoesNotExist
# Create your models here.

class Hotels(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=300,default=" ")
    email = models.EmailField()

    #address
    landmark = models.CharField(max_length=50,default=" ")
    city = models.CharField(max_length=50, default=" ")
    state = models.CharField(max_length=50,default=" ")
    country = models.CharField(max_length=50,default=" ")
    pincode = models.IntegerField(default=00)

    #contacts
    prefix = models.CharField(max_length=4,default=" ")
    phone = models.CharField(max_length=10,default=" ")
    # phone=models.BigIntegerField(max_length=10)

    #accessiblity
    visual_impaired=models.BooleanField(default=0)
    wheelchair_user=models.BooleanField(default=0)
    hearing_impaired=models.BooleanField(default=0)
    speech_impaired=models.BooleanField(default=0)
    
    #extra
    facility = models.TextField(default=" ")
    # rooms = models.IntegerField()
    # price = models.IntegerField()
    # ac_rooms = models.BooleanField()
    roomtype1=models.CharField(max_length=100,default="Regular")
    roomtype2=models.CharField(max_length=100,default="Regular")
    roomtype3=models.CharField(max_length=100,default="Regular")
    pricetype1=models.IntegerField(default=1000)
    pricetype2=models.IntegerField(default=1000)
    pricetype3=models.IntegerField(default=1000)
    facilityoftype1=models.TextField(default=" ")
    facilityoftype2=models.TextField(default=" ")
    facilityoftype3=models.TextField(default=" ")


    image=models.CharField(max_length=500,default=" ")
    
    def __str__(self):
        return self.name
